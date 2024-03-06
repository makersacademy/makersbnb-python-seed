# File: tests/test_guest_manager.py
import pytest
from lib.guest_manager import GuestManager

def test_add_guest():
    guest_manager = GuestManager()
    guest_manager.add_guest("Adam", "password123")
    assert len(guest_manager.guests) == 1
    assert guest_manager.guests[0].username == "Adam"
    assert guest_manager.guests[0].password == "password123"

def test_get_guest():
    guest_manager = GuestManager()
    guest_manager.add_guest("Adam", "password123")
    adam_guest = guest_manager.get_guest("Adam")
    assert adam_guest is not None
    assert adam_guest.username == "Adam"
    assert adam_guest.password == "password123"

def test_get_guest_nonexistent():
    guest_manager = GuestManager()
    non_existent_guest = guest_manager.get_guest("NonExistentUser")
    assert non_existent_guest is None
