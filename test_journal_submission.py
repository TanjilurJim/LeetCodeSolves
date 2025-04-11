import pytest
from check import Author, Manuscript, Reviewer, Administrator, ManuscriptStatus

# Test Case 1: Test Author Registration and Authentication
def test_author_registration_and_login():
    # Create Author
    author = Author("author@example.com", "password123")

    # Test valid login
    assert author.login("password123") == True, "Login failed with correct credentials"

    # Test invalid login
    assert author.login("wrongpassword") == False, "Login succeeded with incorrect credentials"


# Test Case 2: Test Manuscript Submission
def test_manuscript_submission():
    author = Author("author@example.com", "password123")
    co_authors = ["coauthor1@example.com"]  # List of co-authors
    manuscript = Manuscript("Sample Paper", "This is the content of the manuscript.", author, co_authors)

    # Login author before submission
    author.login("password123")

    # Test manuscript submission
    # The manuscript is automatically under review after submission, so no need to call `submit()`.
    assert manuscript.status == ManuscriptStatus.UNDER_REVIEW, "Manuscript status is not correct after submission"


# Test Case 3: Test Review Assignment by Administrator
def test_review_assignment():
    admin = Administrator("admin@example.com", "adminpass")
    reviewer1 = Reviewer("reviewer1@example.com", "reviewerpassword", "Computer Science")

    # Create manuscript and assign reviewer
    co_authors = ["coauthor1@example.com"]
    manuscript = Manuscript("Sample Paper", "This is content", admin, co_authors)

    admin.login("adminpass")
    admin.assign_reviewers(manuscript, [reviewer1])

    # Verify if the manuscript is assigned to reviewer1
    assert manuscript in reviewer1.assigned_manuscripts, "Manuscript was not assigned to reviewer"
    assert manuscript.status == ManuscriptStatus.UNDER_REVIEW, "Manuscript status is not correct after assignment"


# Test Case 4: Test Review Submission by Reviewer
def test_review_submission():
    reviewer = Reviewer("reviewer@example.com", "reviewerpassword", "Computer Science")
    co_authors = ["coauthor1@example.com"]
    manuscript = Manuscript("Sample Paper", "This is content", reviewer, co_authors)

    reviewer.login("reviewerpassword")

    # Submit review
    feedback = "This is a good paper, minor revisions needed."
    decision = "REVISION"

    assert reviewer.submit_review(manuscript, feedback, decision) == True, "Review submission failed"

    # Verify if the review is added
    assert len(manuscript.reviews) == 1, "Review was not added to manuscript"
    assert manuscript.reviews[0].feedback == feedback, "Review feedback does not match"
    assert manuscript.reviews[0].decision == decision, "Review decision is not correct"


# Test Case 5: Test Final Decision by Administrator
def test_final_decision():
    admin = Administrator("admin@example.com", "adminpass")
    co_authors = ["coauthor1@example.com"]
    manuscript = Manuscript("Sample Paper", "This is content", admin, co_authors)

    admin.login("adminpass")

    # Submit a review to make final decision
    feedback = "Accepted with minor revisions."
    decision = "ACCEPT"

    admin.make_final_decision(manuscript, decision, feedback)

    # Verify final decision and manuscript status
    assert manuscript.final_decision == "ACCEPT", "Final decision was not set correctly"
    assert manuscript.status == ManuscriptStatus.ACCEPTED, "Manuscript status was not updated after acceptance"
    assert manuscript.final_feedback == feedback, "Final feedback does not match"


# Test Case 6: Test Manuscript Status Change
def test_manuscript_status_change():
    author = Author("author@example.com", "password123")
    co_authors = ["coauthor1@example.com"]
    manuscript = Manuscript("Sample Paper", "This is the content of the manuscript.", author, co_authors)

    # Initially, the status should be 'Submitted'
    assert manuscript.status == ManuscriptStatus.SUBMITTED, "Manuscript status is not correct initially"

    # Change status to 'Under Review' after assignment
    admin = Administrator("admin@example.com", "adminpass")
    admin.login("adminpass")
    admin.assign_reviewers(manuscript, [Reviewer("reviewer1@example.com", "reviewerpassword", "CS")])

    assert manuscript.status == ManuscriptStatus.UNDER_REVIEW, "Manuscript status did not update correctly"


if __name__ == "__main__":
    pytest.main()
