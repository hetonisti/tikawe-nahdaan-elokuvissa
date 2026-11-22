CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE Events (
    id INTEGER PRIMARY KEY,
    movie TEXT NOT NULL,
    location TEXT NOT NULL,
    showtime DATETIME NOT NULL,
    created_on DATETIME NOT NULL,
    
    UNIQUE (movie, location, showtime)
);

CREATE TABLE Can_modify_event (
    id INTEGER PRIMARY KEY,
    event_id REFERENCES Events NOT NULL,
    user_id REFERENCES Users NOT NULL
);

CREATE TABLE Seeings (
    id INTEGER PRIMARY KEY,
    event_id INTEGER NOT NULL,
    user_id REFERENCES Users NOT NULL,
    
    UNIQUE (event_id, user_id)
);

Create TABLE Tags (
    id INTEGER PRIMARY KEY,
    tag TEXT NOT NULL
);

CREATE TABLE Taggings (
    id INTEGER PRIMARY KEY,
    tag_id REFERENCES Tags NOT NULL,
    event_id REFERENCES Events NOT NULL,
    user_id REFERENCES Users NOT NULL
);

CREATE TABLE Messages (
    id INTEGER PRIMARY KEY,
    event_id REFERENCES Events NOT NULL,
    user_id REFERENCES Users NOT NULL,
    created_on DATETIME NOT NULL,
    message TEXT NOT NULL
);