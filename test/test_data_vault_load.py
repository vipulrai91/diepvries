from .conftest import clean_sql


def test_staging_table_sql(test_path, data_vault_load):
    """
    Compares staging table creation SQL generated by DataVaultLoad with the expected results.

    Args:
        test_path (Path): test_path fixture value (defined in conftest.py).
        data_vault_load (DataVaultLoad): data_vault_load fixture value (defined in conftest.py).
    """
    expected_results = (test_path / "sql" / "expected_results_staging.sql").read_text()
    assert clean_sql(expected_results) == clean_sql(
        data_vault_load.staging_create_sql_statement
    )


def test_data_vault_load_sql(test_path, data_vault_load):
    """
    Compares full DataVault load script generated by DataVaultLoad with the expected results.

    Args:
        test_path (Path): test_path fixture value (defined in conftest.py).
        data_vault_load (DataVaultLoad): data_vault_load fixture value (defined in conftest.py).
    """
    expected_results = (
        (test_path / "sql" / "expected_results_data_vault_load.sql")
        .read_text()
        .split(";")
    )
    for index, sql in enumerate(expected_results):
        if clean_sql(sql) == "":
            break

        assert clean_sql(sql) == clean_sql(data_vault_load.sql_load_script[index])
