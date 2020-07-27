CREATE TRIGGER autoPlannedMaintenance
ON app_component
AFTER INSERT
AS
INSERT INTO db_owner.app_planedmaintenance([plmaindate]
      ,[plmaindescription]
      ,[component_id])
SELECT GETDATE()+c.maintenanceintervall,c.description,c.id
FROM app_component AS c
INNER JOIN inserted AS i
ON c.id= i.id;