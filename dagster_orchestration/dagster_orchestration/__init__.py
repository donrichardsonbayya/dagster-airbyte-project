from dagster import Definitions, AssetSelection, ScheduleDefinition, load_assets_from_modules, define_asset_job

from .assets import resources, dbt_assets_from_project, airbyte_assets

# Combine all assets - handle both list and single asset cases
if isinstance(airbyte_assets, list):
    all_assets = dbt_assets_from_project + airbyte_assets
else:
    all_assets = dbt_assets_from_project + [airbyte_assets]

big_star_job = define_asset_job("big_star_job", selection=AssetSelection.all())

big_star_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule="0 * * * *",  # every hour
)

defs = Definitions(
    assets=all_assets, 
    resources=resources, 
    jobs=[big_star_job], 
    schedules=[big_star_schedule]
)
