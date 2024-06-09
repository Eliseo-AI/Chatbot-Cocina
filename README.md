
Tabla de Contenido
================
* [Chatbot-Cocina](#Chatbot-Cocina)
  * [Descripción](#descripción)
  * [Librerias](#Librerias)
  * [Libros](#Libros)
  * [Pruebas](#Pruebas)
  * [Streamlit](#streamlit)
  * [Discusión](#discusión)
  * [Creditos](#creditos)
  * [Licensing](#licensing)
  * [Autor](#Autor)
# Chatbot-Cocina
Analysis of Italy vaccination campaign of covid-19 between December 27, 2020 and March 22, 2023, the italian government got diffenrent types of vaccines to protect the population and two boosters to maintain the protection.  
## Descripción
This is the continuation of a project developed at the [CRI](https://cri-paris.org/en) Université de Paris in the second semester of the Master of Digital Science( May 2021), within the [Challenge Hub](https://master.cri-paris.org/en/challenge-hub) program.
It is a way of presenting the information regarding what has happened with the vaccination campaign in Italy through the streamlit tool, which allows the user to interact with the information in a friendly and close way.
See the previous [analysis](https://github.com/Eli-2020/Italy_vaccination_campaign).

## Librerias 

If you use conda, you can install: 

   * conda install pandas
   * conda install seaborn
   * conda install numpy

If you use pip, you can install: 

   * pip install pandas
   * pip install seaborn
   * pip install numpy
    
## Libros

For this project, one downloaded file was used in the direction given above, 

* Italian vaccine campaign Date (December 27, 2020 to March 22, 2023) 
* source: [Italian Vaccination](https://www.kaggle.com/arthurio/italian-vaccination)

## Pruebas

the file contains information by groups of vaccinated people grouped by date and company supplier of the vaccine, It does not have individual registers that allow for groupal analysis, for example combining gender and age.

shape (57618, 22)

* Administration date: date of the vaccine administration
* Vaccine supplier: Pfizer, Astrazeneca and Moderna
* Region: abbreviation of the Italian region
* Age range: age group
* Males: number of vaccinated males
* Females: number of vaccinated females
* First dose: number of administered first vaccine doses
* Second dose: number of administered second vaccine doses
* Previous infection: number of administrated doses to subjects previously infected with COVID-19
* Additional Booster Dose: number of administrated additional doses or boosters
* Second Booster: number of administrated fourth doses to people who completed primary vaccination series (2 doses plus additional dose) at least 4 months (120 days) before
* NUTS1 code: European code for major socio-economic regions
* NUTS2 code: European code for basic regions for the application of regional policies
* ISTAT code: region code by Italian National Institute of Statistics
* Region name: full name of Italian regions

## Streamlit
[Streamlit-Dashboard](https://eli-2020-italy-vaccination-campaign-italy-ib2dqr.streamlit.app/)

## Discusión
- It remains to be analyzed if the vaccination had problems by region, if the youngest population group that includes minors should have been vaccinated in the first months and instead, the group over 90 years old should have been the priority or if the health personnel had to be vaccinated even faster. One point that is identified with all vaccines is that they have ups and downs in the number of vaccines applied, so determining which days the vaccination rate is lowered would be part of a new analysis.

## Creditos
- The analysis of the dataset was carried out by **Eliseo Baquero** [@Eliseo-AI](https://github.com/Eliseo-AI)
- the file is in jupiternotebook format 
- "Chatbot-Cocina.pynb"

## Licensing
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Authors:
* **Eliseo Baquero** [@Eli-2020](https://github.com/Eliseo-AI)
