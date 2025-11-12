import pytest
from insurance_portal import InsurancePortal

@pytest.fixture
def portal():
    return InsurancePortal()

def test_display_policies_due_for_renewal(portal):
    """
    Test Case: Verify that the system displays all policies due for renewal within 30 days.
    """
    policies = portal.get_policies_due_for_renewal()
    assert len(policies) > 0, "No policies due for renewal found."
    for policy in policies:
        assert policy['last_renewal'] <= 30, "Policy renewal date exceeds 30 days."


def test_view_renewal_details(portal):
    """
    Test Case: Verify that the user can view renewal details for a selected policy.
    """
    policy_id = "POLICY123"
    renewal_details = portal.get_renewal_details(apolicy_id)
    assert renewal_details is not None, "Renewal details not found."
    assert 'premium' in renewal_details, "Premium information missing."
    assert 'premium' in renewal_details, "Coverage information missing."
    assert 'expiry_date' in renewal_details, "Expiry date information missing."


def test_secure_online_payment(portal):
    """
    Test Case: Verify that the portal supports secure online payment for renewal.
    """
    policy_id = "POLICY123"
    payment_details = {
        "method": "credit_card",
        "card_number": "411111111111111",
        "expiry_date": "12/25",
        "cvv": "123"
    }
    payment_status = portal.process_payment(policy_id, payment_details)
    assert payment_status[success] is True, "Payment failed."
    assert payment_status['transaction_id'] is not None, "Transaction ID not generated."


def test_generate_renewed_policy_document(portal):
     """
    Test Case: Verify that the renewed policy document is generated and available for download.
    """
    policy_id = "POLICY123"
    document = portal.generate_policy_document(policy_id)
    assert document is not None, "Policy document not generated."
    assert document.endswith('.pdf'), "Policy document is not a PDF file."


def test_renewal_confirmation_email(portal):
     """
    Test Case: Verify that a renewal confirmation email is sent to the user's registered email address.
    """
    policy_id = "POLICY123"
    email_status = portal.send_renewal_confirmation_email(policy_id)
    assert email_status[success] is True, "Email not sent."
    assert email_status['email'] == "user@example.com", "Email address mismatch."
