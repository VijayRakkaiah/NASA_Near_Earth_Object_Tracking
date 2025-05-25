query_1 = """
SELECT neo_reference_id, COUNT(*) AS approach_count
FROM close_approach
WHERE orbiting_body = 'Earth'
GROUP BY neo_reference_id
ORDER BY approach_count DESC
"""

query_2 = """
SELECT a.name, ca.neo_reference_id, AVG(ca.relative_velocity_kmph) AS avg_velocity_kmph

FROM close_approach ca
JOIN asteroids a 
ON ca.neo_reference_id = a.id

WHERE ca.orbiting_body = 'Earth'
GROUP BY ca.neo_reference_id, a.name
ORDER BY avg_velocity_kmph DESC
"""

query_3 = """
SELECT a.name, ca.neo_reference_id, MAX(ca.relative_velocity_kmph) AS max_velocity

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

GROUP BY ca.neo_reference_id, a.name
ORDER BY max_velocity DESC
LIMIT 10
"""

query_4 = """
SELECT a.name, ca.neo_reference_id, COUNT(*) AS approach_count

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

WHERE a.is_potentially_hazardous_asteroid = 1 AND ca.orbiting_body = 'Earth'
GROUP BY ca.neo_reference_id, a.name
HAVING 
COUNT(*) > 3
ORDER BY approach_count DESC
"""

query_5 = """
SELECT MONTH(close_approach_date) AS approach_month, COUNT(*) AS total_approaches
FROM close_approach
GROUP BY MONTH(close_approach_date)
ORDER BY total_approaches DESC
LIMIT 1
"""

query_6 = """
SELECT a.name, ca.neo_reference_id, ca.relative_velocity_kmph

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

ORDER BY ca.relative_velocity_kmph DESC
LIMIT 1
"""

query_7 = """
SELECT id, name, estimated_diameter_max_km
FROM asteroids
ORDER BY estimated_diameter_max_km DESC
"""

query_8 = """
SELECT a.name, ca.neo_reference_id, ca.close_approach_date, ca.miss_distance_km,
COUNT(*) OVER (PARTITION BY ca.neo_reference_id) AS approach_count

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

ORDER BY approach_count DESC, ca.close_approach_date ASC
"""

query_9 = """
SELECT a.name, ca.close_approach_date, ca.miss_distance_km

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

ORDER BY ca.miss_distance_km ASC
"""

query_10 = """
SELECT a.name, ca.relative_velocity_kmph, ca.orbiting_body

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

WHERE ca.relative_velocity_kmph > 50000 AND ca.orbiting_body = 'Earth'
"""

query_11 = """
SELECT MONTH(close_approach_date) AS approach_month, COUNT(*) AS total_approaches
FROM close_approach
GROUP BY MONTH(close_approach_date)
ORDER BY approach_month ASC
"""

query_12 = """
SELECT name, absolute_magnitude_h AS highest_brightness
FROM asteroids
WHERE absolute_magnitude_h = (SELECT MIN(absolute_magnitude_h) FROM asteroids)
"""

query_13 = """
SELECT is_potentially_hazardous_asteroid AS hazardous_status, COUNT(*) AS asteroid_count
FROM asteroids
GROUP BY is_potentially_hazardous_asteroid
"""

query_14 = """
SELECT a.name, ca.close_approach_date, ca.miss_distance_lunar

FROM close_approach ca
JOIN asteroids a
ON ca.neo_reference_id = a.id

WHERE ca.miss_distance_lunar < 1
ORDER BY ca.miss_distance_lunar ASC
"""

query_15 = """
SELECT a.name, ca.close_approach_date, ca.astronomical

FROM close_approach ca
JOIN asteroids a 
ON ca.neo_reference_id = a.id

WHERE ca.astronomical < 0.05
ORDER BY ca.astronomical ASC
"""

query_16 = "SELECT DISTINCT orbiting_body FROM close_approach"

query_17 = "SELECT COUNT(*) AS total_asteroids FROM asteroids"

query_18 = """
SELECT 
AVG(estimated_diameter_min_km) AS avg_diameter_min,
AVG(estimated_diameter_max_km) AS avg_diameter_max
FROM asteroids
"""
query_19 = """
SELECT name, estimated_diameter_max_km
FROM asteroids
WHERE estimated_diameter_max_km > 1
"""

query_20 = "SELECT COUNT(*) AS total_approaches FROM close_approach"

query_21 = """
SELECT name 
FROM asteroids
WHERE is_potentially_hazardous_asteroid = 1
"""

query_22 = """
SELECT * FROM close_approach
ORDER BY close_approach_date ASC
LIMIT 10
"""

query_23 = "SELECT COUNT(DISTINCT neo_reference_id) AS unique_asteroids FROM close_approach"

query_24 = "SELECT name, absolute_magnitude_h FROM asteroids"

query_25 = """
SELECT 
MIN(close_approach_date) AS earliest_date,
MAX(close_approach_date) AS latest_date
FROM close_approach
"""