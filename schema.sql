CREATE TABLE IF NOT EXISTS "word" (
  "id" SERIAL PRIMARY KEY,
  "created_at" timestamp,
  "word" varchar,
  "weight" int
);

CREATE INDEX IF NOT EXISTS "Counter" ON "word" ("created_at", "word");
