# Student Name: Jaspreet Singh
# Student ID: 202471129
import pytest
import hashlib
import datetime
import unittest
from abc import ABC, abstractmethod
from typing import List, Dict
import re
import uuid
from enum import Enum


class ManuscriptStatus(Enum):
    SUBMITTED = "Submitted"
    UNDER_REVIEW = "Under Review"
    NEEDS_REVISION = "Needs Revision"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class User(ABC):
    """Base class for all users in the system"""

    def __init__(self, email: str, password: str):
        self.email = email
        self.user_id = str(uuid.uuid4())
        # Hash password using SHA-256 (in production, use more secure methods like bcrypt)
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.logged_in = False

    @abstractmethod
    def get_role(self) -> str:
        pass

    def login(self, password: str) -> bool:
        """Authenticate user"""
        if hashlib.sha256(password.encode()).hexdigest() == self.password_hash:
            self.logged_in = True
            return True
        return False

    def logout(self):
        """Log out user"""
        self.logged_in = False


class Author(User):
    """Author class for manuscript submission"""

    def __init__(self, email: str, password: str):
        super().__init__(email, password)
        self.manuscripts: List[Manuscript] = []

    def get_role(self) -> str:
        return "Author"

    def submit_manuscript(self, title: str, content: str, co_authors: List[str]) -> 'Manuscript':
        """Submit a new manuscript"""
        if not self.logged_in:
            raise PermissionError("Author must be logged in to submit manuscript")

        manuscript = Manuscript(title, content, self, co_authors)
        self.manuscripts.append(manuscript)
        return manuscript


class Reviewer(User):
    """Reviewer class for manuscript review"""

    def __init__(self, email: str, password: str, specialization: str):
        super().__init__(email, password)
        self.specialization = specialization
        self.assigned_manuscripts: List[Manuscript] = []

    def get_role(self) -> str:
        return "Reviewer"

    def submit_review(self, manuscript: 'Manuscript', feedback: str, decision: str) -> bool:
        """Submit review for assigned manuscript"""
        if not self.logged_in:
            raise PermissionError("Reviewer must be logged in to submit review")

        if manuscript not in self.assigned_manuscripts:
            raise ValueError("Manuscript not assigned to this reviewer")

        review = Review(self, manuscript, feedback, decision)
        manuscript.add_review(review)
        return True


class Administrator(User):
    """Administrator class for system management"""

    def __init__(self, email: str, password: str):
        super().__init__(email, password)

    def get_role(self) -> str:
        return "Administrator"

    def assign_reviewers(self, manuscript: 'Manuscript', reviewers: List[Reviewer]):
        """Assign reviewers to a manuscript"""
        if not self.logged_in:
            raise PermissionError("Administrator must be logged in to assign reviewers")

        if len(reviewers) > 3:
            raise ValueError("Maximum 3 reviewers can be assigned")

        for reviewer in reviewers:
            manuscript.assign_reviewer(reviewer)
            reviewer.assigned_manuscripts.append(manuscript)

    def make_final_decision(self, manuscript: 'Manuscript', decision: str, feedback: str):
        """Make final decision on manuscript"""
        if not self.logged_in:
            raise PermissionError("Administrator must be logged in to make decision")

        if len(manuscript.reviews) < 1:
            raise ValueError("Cannot make decision without reviews")

        manuscript.set_final_decision(decision, feedback)


class Manuscript:
    """Manuscript class representing submitted papers"""

    def __init__(self, title: str, content: str, author: Author, co_authors: List[str]):
        self.manuscript_id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.author = author
        self.co_authors = co_authors
        self.submission_date = datetime.datetime.now()
        self.status = ManuscriptStatus.SUBMITTED
        self.reviews: List[Review] = []
        self.assigned_reviewers: List[Reviewer] = []
        self.final_decision = None
        self.final_feedback = None

    def assign_reviewer(self, reviewer: Reviewer):
        """Assign a reviewer to the manuscript"""
        if len(self.assigned_reviewers) >= 3:
            raise ValueError("Maximum reviewers already assigned")
        self.assigned_reviewers.append(reviewer)
        self.status = ManuscriptStatus.UNDER_REVIEW

    def add_review(self, review: 'Review'):
        """Add a review to the manuscript"""
        self.reviews.append(review)

    def set_final_decision(self, decision: str, feedback: str):
        """Set final decision on manuscript"""
        self.final_decision = decision
        self.final_feedback = feedback
        if decision == "ACCEPT":
            self.status = ManuscriptStatus.ACCEPTED
        elif decision == "REJECT":
            self.status = ManuscriptStatus.REJECTED
        else:
            self.status = ManuscriptStatus.NEEDS_REVISION


class Review:
    """Review class for manuscript feedback"""

    def __init__(self, reviewer: Reviewer, manuscript: Manuscript, feedback: str, decision: str):
        self.review_id = str(uuid.uuid4())
        self.reviewer = reviewer
        self.manuscript = manuscript
        self.feedback = feedback
        self.decision = decision
        self.submission_date = datetime.datetime.now()


class JournalSystem:
    """Main system class managing all operations"""

    def __init__(self):
        self.users: Dict[str, User] = {}
        self.manuscripts: Dict[str, Manuscript] = {}
        self.current_user: User = None

    def register_user(self, email: str, password: str, role: str, specialization: str = None) -> User:
        """Register a new user in the system"""
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")

        # Validate password strength
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        # Create appropriate user type
        if role.lower() == "author":
            user = Author(email, password)
        elif role.lower() == "reviewer":
            if not specialization:
                raise ValueError("Reviewer must have a specialization")
            user = Reviewer(email, password, specialization)
        elif role.lower() == "administrator":
            user = Administrator(email, password)
        else:
            raise ValueError("Invalid role")

        self.users[email] = user
        return user

    def login_user(self, email: str, password: str) -> bool:
        """Login a user"""
        if email in self.users:
            user = self.users[email]
            if user.login(password):
                self.current_user = user
                return True
        return False

    def logout_user(self):
        """Logout current user"""
        if self.current_user:
            self.current_user.logout()
            self.current_user = None


def main():
    """Main function demonstrating system usage"""
    system = JournalSystem()

    # Example usage
    try:
        # Register users
        author = system.register_user("author@example.com", "password123", "author")
        reviewer = system.register_user("reviewer@example.com", "password123", "reviewer", "Computer Science")
        admin = system.register_user("admin@example.com", "password123", "administrator")

        # Login as author and submit manuscript
        system.login_user("author@example.com", "password123")
        manuscript = author.submit_manuscript(
            "Sample Paper",
            "This is a sample paper content.",
            ["co-author1@example.com"]
        )

        # Login as admin and assign reviewer
        system.login_user("admin@example.com", "password123")
        admin.assign_reviewers(manuscript, [reviewer])

        # Login as reviewer and submit review
        system.login_user("reviewer@example.com", "password123")
        reviewer.submit_review(
            manuscript,
            "This is a good paper with minor revisions needed.",
            "REVISION"
        )

        # Admin makes final decision
        system.login_user("admin@example.com", "password123")
        admin.make_final_decision(manuscript, "ACCEPT", "Paper accepted with minor revisions")

        print(f"Manuscript Status: {manuscript.status.value}")
        print(f"Final Decision: {manuscript.final_decision}")
        print(f"Feedback: {manuscript.final_feedback}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    unittest.main()