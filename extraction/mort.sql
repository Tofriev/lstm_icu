WITH mort AS (
    SELECT
        ic.subject_id,
        ic.stay_id,
        ic.hadm_id,
        CASE
          WHEN 
            adm.deathtime BETWEEN datetime(ic.intime, '+25 hours') AND ic.outtime THEN 1
            ELSE 0
        END AS Mortality_icu    
    FROM icustays ic
    INNER JOIN admissions adm ON ic.hadm_id = adm.hadm_id
)
SELECT
  m.Mortality_icu AS mortality,
  ic.stay_id
FROM
  icustays ic
INNER JOIN mort AS m ON ic.stay_id = m.stay_id
ORDER BY
  ic.stay_id;
