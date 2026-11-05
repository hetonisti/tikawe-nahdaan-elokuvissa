CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE Events (
    id INTEGER PRIMARY KEY,
    movie TEXT NOT NULL,
    place TEXT NOT NULL,
    showtime DATETIME NOT NULL,
    created_on DATETIME NOT NULL,
    user1_id INTEGER NOT NULL,
    user2_id INTEGER NOT NULL,
    
    UNIQUE (movie, place, showtime),
    CHECK (user1_id <> user2_id),

    FOREIGN KEY (id, user1_id)
        REFERENCES Seeings (event_id, id)
        DEFERRABLE INITIALLY DEFERRED,
    
    FOREIGN KEY (id, user2_id)
        REFERENCES Seeings (event_id, id)
        DEFERRABLE INITIALLY DEFERRED
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
    
    UNIQUE (event_id, id),
    UNIQUE (event_id, user_id),

    FOREIGN KEY (event_id)
        REFERENCES Events (id)
        DEFERRABLE INITIALLY DEFERRED
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