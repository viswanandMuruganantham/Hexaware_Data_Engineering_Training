CREATE DATABASE smart_home_energy;

USE smart_home_energy;
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_name VARCHAR(100)
);

CREATE TABLE devices (
    device_id INT PRIMARY KEY AUTO_INCREMENT,
    device_name VARCHAR(100),
    room_id INT,
    device_type VARCHAR(50),
    status VARCHAR(20),

    FOREIGN KEY (room_id)
    REFERENCES rooms(room_id)
);

CREATE TABLE energy_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    device_id INT,
    energy_kwh DECIMAL(10,2),
    usage_time TIMESTAMP,

    FOREIGN KEY (device_id)
    REFERENCES devices(device_id)
);

INSERT INTO rooms(room_name)
VALUES
('Living Room'),
('Kitchen'),
('Bedroom');

INSERT INTO devices(
    device_name,
    room_id,
    device_type,
    status
)
VALUES
('Air Conditioner', 1, 'Cooling', 'ON'),
('Refrigerator', 2, 'Appliance', 'ON'),
('LED TV', 1, 'Entertainment', 'OFF'),
('Fan', 3, 'Cooling', 'ON');

INSERT INTO energy_logs(
    device_id,
    energy_kwh,
    usage_time
)
VALUES
(1, 5.5, '2026-05-01 10:00:00'),
(2, 2.1, '2026-05-01 11:00:00'),
(3, 1.2, '2026-05-01 12:00:00'),
(4, 0.8, '2026-05-01 13:00:00');

INSERT INTO energy_logs(
    device_id,
    energy_kwh,
    usage_time
)
VALUES
(1, 6.0, NOW());

SELECT
d.device_name,
r.room_name,
e.energy_kwh,
e.usage_time
FROM energy_logs e
JOIN devices d
ON e.device_id = d.device_id
JOIN rooms r
ON d.room_id = r.room_id;

UPDATE devices
SET status = 'OFF'
WHERE device_id = 1;

DELETE FROM energy_logs
WHERE log_id = 4;

DELIMITER $$

CREATE PROCEDURE GetDailyRoomUsage(
    IN input_date DATE
)
BEGIN
    SELECT
        r.room_name,
        SUM(e.energy_kwh) AS total_energy
    FROM energy_logs e
    JOIN devices d
        ON e.device_id = d.device_id
    JOIN rooms r
        ON d.room_id = r.room_id
    WHERE DATE(e.usage_time) = input_date
    GROUP BY r.room_name;
END $$

DELIMITER ;

CALL GetDailyRoomUsage('2026-05-01');