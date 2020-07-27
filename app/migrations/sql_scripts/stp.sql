CREATE PROCEDURE [db_owner].[autoIncrementComponent]
(
@ComponentID int,
@Count int
)
as
DECLARE @exists int =0
SELECT @exists = count(*)
FROM  app_component
WHERE app_component.id= @ComponentID
IF(@count=1)
BEGIN
UPDATE app_component SET currentcyclecounter=@Count
WHERE id=@ComponentID
END
ELSE
print'Component Doesnt Exist'