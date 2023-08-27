function createUser(email, password) {
    try {
        validateInput(email, password);
    } catch (e) {
        showErrorMessage(e.message);
    }

    saveUser(email, password);
}

function validateInput(email, password) {
    if (!isValidInput(email, password)) {
        throw new Error("Invalid input");
    }
}

function isValidInput(email, password) {
    if (!isEmail(email) || !isPassword(password)) {
        return false;
    }

    return true;
}

function isEmail(email) {
    if (!email || !email.includes("@")) {
        return false;
    }

    return true;
}

function isPassword(password) {
    if (!password || password.trim() === "") {
        return false;
    }

    return true;
}

function showErrorMessage($message) {
    console.error($message);
}

function saveUser(email, password) {
    const user = {
        email: email,
        password: password,
    };

    database.insert(user);
}
