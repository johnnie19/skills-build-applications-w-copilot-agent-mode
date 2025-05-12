// Initialize the MongoDB database and collections for OctoFit Tracker

// Connect to the octofit_db database
use octofit_db;

// Create users collection with a unique index on email
db.users.createIndex({ "email": 1 }, { unique: true });

// Create teams collection
db.createCollection("teams");

// Create activity collection
db.createCollection("activity");

// Create leaderboard collection
db.createCollection("leaderboard");

// Create workouts collection
db.createCollection("workouts");
