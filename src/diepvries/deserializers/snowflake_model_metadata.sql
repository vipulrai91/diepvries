/*Query that fetches all needed properties to initialize a StagingTable and all DataVaultTable objects*/
SELECT
  LOWER(columns.table_name)                   AS "table",
  LOWER(columns.column_name)                  AS "field",
  UPPER(columns.data_type)                    AS "data_type",
  columns.ordinal_position::INTEGER           AS "position",
  NOT (TO_BOOLEAN(columns.is_nullable))       AS "is_mandatory",
  columns.numeric_precision::INTEGER          AS "precision",
  columns.numeric_scale::INTEGER              AS "scale",
  columns.character_maximum_length::INTEGER   AS "length"
FROM information_schema.columns AS columns
WHERE columns.table_schema = UPPER('{target_schema}')
  AND LOWER(table_name) IN ({table_list})
  AND SPLIT_PART(LOWER(table_name), '_', 1) IN ({table_prefixes});