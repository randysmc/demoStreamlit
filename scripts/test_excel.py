
from src.ingestion.excel_reader import read_excel_file
from src.validation.data_validator import validate_dataframe

from src.analytics.epidemiological_analysis import (
    cases_by_disease,
    cases_by_department,
    cases_by_month,
    cases_by_age_group,
    cases_by_sex
)


def main():

    file_path = "storage/raw/sala_situacional_demo.xlsx"

    dataframe = read_excel_file(file_path)

    # Validación
    validation = validate_dataframe(dataframe)

    print("\n========== CALIDAD DE DATOS ==========")

    for name, result in validation.items():
        print(f"{name}: {result}")

    # por enfermedad
    print("\n========== CASOS POR ENFERMEDAD ==========")
    print(cases_by_disease(dataframe).to_string(index=False))

    # por departamento
    print("\n========== CASOS POR DEPARTAMENTO ==========")
    print(cases_by_department(dataframe).to_string(index=False))

    # mensual
    print("\n========== CASOS POR MES ==========")
    print(cases_by_month(dataframe).to_string(index=False))

    # por edad
    print("\n========== CASOS POR GRUPO DE EDAD ==========")
    print(cases_by_age_group(dataframe).to_string(index=False))

    # por sexo
    print("\n========== CASOS POR SEXO ==========")
    print(cases_by_sex(dataframe).to_string(index=False))


if __name__ == "__main__":
    main()
