**Title:** 
<br>User Registration

**User Story:**
<br>As a potential user of the BnB site, I want to be able to register for an account so that I can access personalized features and interact with the platform.

**Acceptance Criteria:**
1. As a new user, I should be able to access the registration page.
2. On the registration page, I should see fields to enter my name, email address, password, and other required details.
3. After filling in the registration form, I should be able to submit it.
4. If the registration is successful, I should receive a confirmation message and be redirected to the login page.

**Database Design:**
Table name: users
Parameters: id, name, username, password, email

```sql
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    password TEXT
);
```

**Classes:**
User
    Constructor
UserRepository
    Add
    Get by username

