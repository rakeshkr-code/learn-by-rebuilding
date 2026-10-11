import sys
import pysqlite3 as sqlite


MIN_SQLITE_VERSION = (3, 45, 0)


def parse_version(version: str) -> tuple[int, int, int]:
    parts = version.split(".")
    return tuple(int(part) for part in parts[:3])


def main() -> None:
    # used an in-memory database for this test only. 
    # It disappears when the connection closes, so no test database file is created. 
    conn = sqlite.connect(":memory:")

    try:
        sqlite_version = conn.execute(
            "SELECT sqlite_version()"
        ).fetchone()[0]

        print(f"Python version: {sys.version.split()[0]}")
        print(f"pysqlite3 module: {sqlite.__file__}")
        print(f"SQLite engine version: {sqlite_version}")

        if parse_version(sqlite_version) < MIN_SQLITE_VERSION:
            raise RuntimeError(
                "SQLite 3.45.0 or newer is required for JSONB."
            )

        sample_json = (
            '{"country":"India","state":"West Bengal",'
            '"city":"Kolkata"}'
        )

        result = conn.execute(
            """
            SELECT
                typeof(jsonb(?)),
                json_extract(jsonb(?), '$.city'),
                json_valid(jsonb(?), 8)
            """,
            (sample_json, sample_json, sample_json),
        ).fetchone()

        storage_type, city, is_valid_jsonb = result

        print(f"JSONB storage class: {storage_type}")
        print(f"Extracted city: {city}")
        print(f"Valid SQLite JSONB: {is_valid_jsonb}")

        assert storage_type == "blob"
        assert city == "Kolkata"
        assert is_valid_jsonb == 1

        print("\nEnvironment check passed.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()