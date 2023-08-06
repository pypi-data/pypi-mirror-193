from importlib.metadata import version

__name__ = "airflow-provider-bigquery-reservation"
__version__ = version(__name__)


def get_provider_info():
    return {
        "package-name": __name__,
        "name": "Apache Airflow BigQuery Reservation Provider",
        "description": "Airflow Provider to buy reservation in BigQuery",
        "connection-types": [
            {
                "connection-type": "google_cloud_platform",
                "hook-class-name": "bigquery_reservation.hooks.bigquery_reservation.BigQueryReservationServiceHook",
            }
        ],
        "extra-links": [
            "bigquery_reservation.operators.bigquery_reservation.BigQueryReservationCreateOperator",
            "bigquery_reservation.operators.bigquery_reservation.BigQueryReservationDeleteOperator",
            "bigquery_reservation.operators.bigquery_reservation.BigQueryBiEngineReservationCreateOperator",
            "bigquery_reservation.operators.bigquery_reservation.BigQueryBiEngineReservationDeleteOperator",
        ],
        "versions": [__version__],
    }
