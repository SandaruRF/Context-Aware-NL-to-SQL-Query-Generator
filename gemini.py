from google import genai

client = genai.Client(api_key="AIzaSyA3bDMjrM1pyDSFvLs8j0DH2rR0Xd11xRE")

schema_info = """{
  "metadata": [
    {
      "table_name": "artist",
      "columns": [
        {
          "column_name": "artist_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "name",
          "data_type": "VARCHAR(120)"
        }
      ],
      "primary_keys": [
        "artist_id"
      ],
      "foreign_keys": []
    },
    {
      "table_name": "album",
      "columns": [
        {
          "column_name": "album_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "title",
          "data_type": "VARCHAR(160)"
        },
        {
          "column_name": "artist_id",
          "data_type": "INTEGER"
        }
      ],
      "primary_keys": [
        "album_id"
      ],
      "foreign_keys": [
        {
          "local_column": "artist_id",
          "referenced_table": "artist",
          "referenced_column": "artist_id"
        }
      ]
    },
    {
      "table_name": "employee",
      "columns": [
        {
          "column_name": "employee_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "last_name",
          "data_type": "VARCHAR(20)"
        },
        {
          "column_name": "first_name",
          "data_type": "VARCHAR(20)"
        },
        {
          "column_name": "title",
          "data_type": "VARCHAR(30)"
        },
        {
          "column_name": "reports_to",
          "data_type": "INTEGER"
        },
        {
          "column_name": "birth_date",
          "data_type": "TIMESTAMP"
        },
        {
          "column_name": "hire_date",
          "data_type": "TIMESTAMP"
        },
        {
          "column_name": "address",
          "data_type": "VARCHAR(70)"
        },
        {
          "column_name": "city",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "state",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "country",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "postal_code",
          "data_type": "VARCHAR(10)"
        },
        {
          "column_name": "phone",
          "data_type": "VARCHAR(24)"
        },
        {
          "column_name": "fax",
          "data_type": "VARCHAR(24)"
        },
        {
          "column_name": "email",
          "data_type": "VARCHAR(60)"
        }
      ],
      "primary_keys": [
        "employee_id"
      ],
      "foreign_keys": [
        {
          "local_column": "reports_to",
          "referenced_table": "employee",
          "referenced_column": "employee_id"
        }
      ]
    },
    {
      "table_name": "customer",
      "columns": [
        {
          "column_name": "customer_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "first_name",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "last_name",
          "data_type": "VARCHAR(20)"
        },
        {
          "column_name": "company",
          "data_type": "VARCHAR(80)"
        },
        {
          "column_name": "address",
          "data_type": "VARCHAR(70)"
        },
        {
          "column_name": "city",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "state",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "country",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "postal_code",
          "data_type": "VARCHAR(10)"
        },
        {
          "column_name": "phone",
          "data_type": "VARCHAR(24)"
        },
        {
          "column_name": "fax",
          "data_type": "VARCHAR(24)"
        },
        {
          "column_name": "email",
          "data_type": "VARCHAR(60)"
        },
        {
          "column_name": "support_rep_id",
          "data_type": "INTEGER"
        }
      ],
      "primary_keys": [
        "customer_id"
      ],
      "foreign_keys": [
        {
          "local_column": "support_rep_id",
          "referenced_table": "employee",
          "referenced_column": "employee_id"
        }
      ]
    },
    {
      "table_name": "invoice",
      "columns": [
        {
          "column_name": "invoice_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "customer_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "invoice_date",
          "data_type": "TIMESTAMP"
        },
        {
          "column_name": "billing_address",
          "data_type": "VARCHAR(70)"
        },
        {
          "column_name": "billing_city",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "billing_state",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "billing_country",
          "data_type": "VARCHAR(40)"
        },
        {
          "column_name": "billing_postal_code",
          "data_type": "VARCHAR(10)"
        },
        {
          "column_name": "total",
          "data_type": "NUMERIC(10, 2)"
        }
      ],
      "primary_keys": [
        "invoice_id"
      ],
      "foreign_keys": [
        {
          "local_column": "customer_id",
          "referenced_table": "customer",
          "referenced_column": "customer_id"
        }
      ]
    },
    {
      "table_name": "invoice_line",
      "columns": [
        {
          "column_name": "invoice_line_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "invoice_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "track_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "unit_price",
          "data_type": "NUMERIC(10, 2)"
        },
        {
          "column_name": "quantity",
          "data_type": "INTEGER"
        }
      ],
      "primary_keys": [
        "invoice_line_id"
      ],
      "foreign_keys": [
        {
          "local_column": "invoice_id",
          "referenced_table": "invoice",
          "referenced_column": "invoice_id"
        },
        {
          "local_column": "track_id",
          "referenced_table": "track",
          "referenced_column": "track_id"
        }
      ]
    },
    {
      "table_name": "track",
      "columns": [
        {
          "column_name": "track_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "name",
          "data_type": "VARCHAR(200)"
        },
        {
          "column_name": "album_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "media_type_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "genre_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "composer",
          "data_type": "VARCHAR(220)"
        },
        {
          "column_name": "milliseconds",
          "data_type": "INTEGER"
        },
        {
          "column_name": "bytes",
          "data_type": "INTEGER"
        },
        {
          "column_name": "unit_price",
          "data_type": "NUMERIC(10, 2)"
        }
      ],
      "primary_keys": [
        "track_id"
      ],
      "foreign_keys": [
        {
          "local_column": "album_id",
          "referenced_table": "album",
          "referenced_column": "album_id"
        },
        {
          "local_column": "genre_id",
          "referenced_table": "genre",
          "referenced_column": "genre_id"
        },
        {
          "local_column": "media_type_id",
          "referenced_table": "media_type",
          "referenced_column": "media_type_id"
        }
      ]
    },
    {
      "table_name": "genre",
      "columns": [
        {
          "column_name": "genre_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "name",
          "data_type": "VARCHAR(120)"
        }
      ],
      "primary_keys": [
        "genre_id"
      ],
      "foreign_keys": []
    },
    {
      "table_name": "media_type",
      "columns": [
        {
          "column_name": "media_type_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "name",
          "data_type": "VARCHAR(120)"
        }
      ],
      "primary_keys": [
        "media_type_id"
      ],
      "foreign_keys": []
    },
    {
      "table_name": "playlist",
      "columns": [
        {
          "column_name": "playlist_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "name",
          "data_type": "VARCHAR(120)"
        }
      ],
      "primary_keys": [
        "playlist_id"
      ],
      "foreign_keys": []
    },
    {
      "table_name": "playlist_track",
      "columns": [
        {
          "column_name": "playlist_id",
          "data_type": "INTEGER"
        },
        {
          "column_name": "track_id",
          "data_type": "INTEGER"
        }
      ],
      "primary_keys": [
        "playlist_id",
        "track_id"
      ],
      "foreign_keys": [
        {
          "local_column": "playlist_id",
          "referenced_table": "playlist",
          "referenced_column": "playlist_id"
        },
        {
          "local_column": "track_id",
          "referenced_table": "track",
          "referenced_column": "track_id"
        }
      ]
    }
  ]
}"""

nl_query = "give list of all artists"

prompt = f"""Convert the following natural language query into an optimized SQL query.

Schema:
{schema_info}

Query:
{nl_query}

SQL Query:"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)