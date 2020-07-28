DECLARE @ComponentGroupID as INT;
DECLARE @ComponentID as INT;
DECLARE @ComponentGroupAllComponents AS CURSOR;
SET @ComponentGroupAllComponents = CURSOR FOR
SELECT componentgroup_id,component_id
FROM app_componentgroup_component;
OPEN @ComponentGroupAllComponents
FETCH NEXT FROM @ComponentGroupAllComponents INTO @ComponentGroupID,@ComponentID;
WHILE @@FETCH_STATUS= 0
BEGIN PRINT @ComponentGroupID + @ComponentID;
FETCH NEXT FROM @ComponentGroupAllComponents INTO @ComponentGroupID,@ComponentID;
END
CLOSE @ComponentGroupAllComponents;
DEALLOCATE @ComponentGroupAllComponents;