from lib.user import User

# Instantiates with the email and password stored correctly
def test_user_instantiates_correctly():
    user = User(1, "test-email", "test-password")
    assert user.id == 1
    assert user.email == "test-email"
    assert user.password == "test-password"

def test_identical_instances_equal_for_testing():
    user1 = User(1, "test-email", "test-password")
    user2 = User(1, "test-email", "test-password")
    assert user1 == user2
