## Database Schema

> python 03_create_schema.py

Database: 01_sqlite\data\shop.db
Foreign keys enabled: 1

Created tables:

- gallery
  - media_id             INTEGER  NOT NULL=False PRIMARY KEY=True
  - product_id           INTEGER  NOT NULL=False PRIMARY KEY=False
  - name                 TEXT     NOT NULL=True PRIMARY KEY=False
  - mime_type            TEXT     NOT NULL=True PRIMARY KEY=False
  - image_data           BLOB     NOT NULL=True PRIMARY KEY=False
  - metadata_jsonb       BLOB     NOT NULL=False PRIMARY KEY=False
  - created_at           TEXT     NOT NULL=True PRIMARY KEY=False

- itemlist
  - product_id           INTEGER  NOT NULL=False PRIMARY KEY=True
  - name                 TEXT     NOT NULL=True PRIMARY KEY=False
  - description          TEXT     NOT NULL=True PRIMARY KEY=False
  - price_paise          INTEGER  NOT NULL=True PRIMARY KEY=False
  - metadata_jsonb       BLOB     NOT NULL=False PRIMARY KEY=False
  - is_active            INTEGER  NOT NULL=True PRIMARY KEY=False
  - created_at           TEXT     NOT NULL=True PRIMARY KEY=False

- purchases
  - purchase_id          INTEGER  NOT NULL=False PRIMARY KEY=True
  - user_id              INTEGER  NOT NULL=True PRIMARY KEY=False
  - product_id           INTEGER  NOT NULL=True PRIMARY KEY=False
  - quantity             INTEGER  NOT NULL=True PRIMARY KEY=False
  - unit_price_paise     INTEGER  NOT NULL=True PRIMARY KEY=False
  - purchase_time        TEXT     NOT NULL=True PRIMARY KEY=False

- userdata
  - user_id              INTEGER  NOT NULL=False PRIMARY KEY=True
  - full_name_jsonb      BLOB     NOT NULL=True PRIMARY KEY=False
  - email                TEXT     NOT NULL=True PRIMARY KEY=False
  - location_jsonb       BLOB     NOT NULL=False PRIMARY KEY=False
  - created_at           TEXT     NOT NULL=True PRIMARY KEY=False

✅ Schema creation successful.