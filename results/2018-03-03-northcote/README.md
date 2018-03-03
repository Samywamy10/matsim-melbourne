### Northcote trips

This run uses the ABS accurate synthetic population for NORTHCOTE (with respect to `sex`, `age`, `relationship status`), with trips mapped to correct SA2 work destinations and transport mode, for persons of particular characteristics.

In other words, persons of given sex, age, and relationship status are driving to correct SA2 work destinations (albeit random locations within) using correct modes of transport, as per census 2011.

The related scenario is in `scenarios/2018-03-scenario-by-dhi-northcote`.

The output was produced using:
```
mvn clean install -DskipTests
mvn exec:java -Dexec.mainClass="io.github.agentsoz.matsimmelbourne.demand.latch.AssignTripsToPopulationDS"

```
