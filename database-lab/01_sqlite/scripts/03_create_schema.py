from pathlib import Path

import pysqlite3 as sqlite


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
DB_PATH = DATA_DIR / "shop.db"


SCHEMA = """
BEGIN;

CREATE TABLE IF NOT EXISTS userdata (
    user_id INTEGER PRIMARY KEY,

    full_name_jsonb BLOB NOT NULL
        CHECK (json_valid(full_name_jsonb, 8)),

    email TEXT NOT NULL UNIQUE,

    location_jsonb BLOB
        CHECK (
            location_jsonb IS NULL
            OR json_valid(location_jsonb, 8)
        ),

    created_at TEXT NOT NULL
        DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);


CREATE TABLE IF NOT EXISTS itemlist (
    product_id INTEGER PRIMARY KEY,

    name TEXT NOT NULL,

    description TEXT NOT NULL DEFAULT '',

    price_paise INTEGER NOT NULL
        CHECK (price_paise >= 0),

    metadata_jsonb BLOB
        CHECK (
            metadata_jsonb IS NULL
            OR json_valid(metadata_jsonb, 8)
        ),

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    created_at TEXT NOT NULL
        DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);


CREATE TABLE IF NOT EXISTS purchases (
    purchase_id INTEGER PRIMARY KEY,

    user_id INTEGER NOT NULL
        REFERENCES userdata(user_id)
        ON DELETE RESTRICT,

    product_id INTEGER NOT NULL
        REFERENCES itemlist(product_id)
        ON DELETE RESTRICT,

    quantity INTEGER NOT NULL DEFAULT 1
        CHECK (quantity > 0),

    unit_price_paise INTEGER NOT NULL
        CHECK (unit_price_paise >= 0),

    purchase_time TEXT NOT NULL
        DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);


CREATE TABLE IF NOT EXISTS gallery (
    media_id INTEGER PRIMARY KEY,

    product_id INTEGER
        REFERENCES itemlist(product_id)
        ON DELETE SET NULL,

    name TEXT NOT NULL,

    mime_type TEXT NOT NULL,

    image_data BLOB NOT NULL
        CHECK (length(image_data) > 0),

    metadata_jsonb BLOB
        CHECK (
            metadata_jsonb IS NULL
            OR json_valid(metadata_jsonb, 8)
        ),

    created_at TEXT NOT NULL
        DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

COMMIT;
"""


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite.connect(str(DB_PATH))

    try:
        # Enable foreign-key enforcement for this connection.
        conn.execute("PRAGMA foreign_keys = ON")

        foreign_keys_enabled = conn.execute(
            "PRAGMA foreign_keys"
        ).fetchone()[0]

        if foreign_keys_enabled != 1:
            raise RuntimeError("Foreign-key enforcement is disabled.")

        # Create the tables in one explicit transaction.
        conn.executescript(SCHEMA)

        tables = conn.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name
            """
        ).fetchall()

        print(f"Database: {DB_PATH}")
        print(f"Foreign keys enabled: {foreign_keys_enabled}")
        print("\nCreated tables:")

        for (table_name,) in tables:
            print(f"\n{table_name}")

            columns = conn.execute(
                f"PRAGMA table_info({table_name})"
            ).fetchall()

            for column in columns:
                column_name = column[1]
                column_type = column[2]
                not_null = bool(column[3])
                primary_key = bool(column[5])

                print(
                    f"  {column_name:<20} "
                    f"{column_type:<8} "
                    f"NOT NULL={not_null} "
                    f"PRIMARY KEY={primary_key}"
                )

        print("\n✅ Schema creation successful.")

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    main()