import os
from dagster import asset

# Simple dbt assets for now (without Airbyte integration)
@asset(key_prefix=["transformed_data"])
def stg_customers():
    """Staging customers table"""
    return "stg_customers"

@asset(key_prefix=["transformed_data"])
def stg_orders():
    """Staging orders table"""
    return "stg_orders"

@asset(key_prefix=["transformed_data"], deps=[stg_customers, stg_orders])
def dim_customers():
    """Customer dimension table"""
    return "dim_customers"

# Simple raw data assets (representing what would come from Airbyte)
@asset(key_prefix=["raw_data"])
def raw_customers():
    """Raw customers data from PostgreSQL"""
    return "raw_customers"

@asset(key_prefix=["raw_data"])
def raw_orders():
    """Raw orders data from PostgreSQL"""
    return "raw_orders"

@asset(key_prefix=["raw_data"])
def raw_products():
    """Raw products data from PostgreSQL"""
    return "raw_products"

@asset(key_prefix=["raw_data"])
def raw_order_items():
    """Raw order items data from PostgreSQL"""
    return "raw_order_items"

# Export all assets
dbt_assets_from_project = [stg_customers, stg_orders, dim_customers]
airbyte_assets = [raw_customers, raw_orders, raw_products, raw_order_items]

# Empty resources for now
resources = {}

__all__ = ["resources", "dbt_assets_from_project", "airbyte_assets"]