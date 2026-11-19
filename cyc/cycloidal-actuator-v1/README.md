# Cycloidal actuator V1 — final printed components

This package contains Josh’s saved final printed-component set: **26 printed instances**, supplied as **11 STL files**, plus the complete three-plate Bambu Studio project. The quantities are in `parts.csv` and `manifest.json`.

Import the STLs in **millimeters**. STL does not encode units. Individual parts retain their saved print orientation and scale; each is centered in X/Y with its lowest point at Z=0. The original 3MF retains all plate positions and settings. No geometry repairs or dimensional changes were made.

## Printing quantities

| File | Saved source name | Quantity |
|---|---|---:|
| `01-end-effector-torque-test.stl` | end effector torque test | 1 |
| `02-pin.stl` | Pin | 1 |
| `03-motor-attachment.stl` | Motor Attachment | 1 |
| `04-output-shaft.stl` | output shaft | 1 |
| `05-top-cap.stl` | Top Cap | 1 |
| `06-planetary-disk-01.stl` | Planetary disk | 1 |
| `07-planetary-disk-02.stl` | Planetary disk | 1 |
| `08-output-shaft-attach.stl` | Output Shaft Attach | 1 |
| `09-eccentric-shaft-1.stl` | eccentric shaft (1) | 1 |
| `10-motor-shaft-lock.stl` | motor shaft lock | 1 |
| `11-spacer-16.stl` | Spacer 16 | 16 |

The source name `Pin` refers to the large housing-like ring visible in the saved project; it is not a steel-dowel instruction. Both disk source objects are retained as separate files. `Spacer 16` is the saved label: print 16 instances; its mesh height is 6 mm.

## Saved slice estimate

The matching saved slices estimate **296.56 g** total, using Bambu PLA Basic, a P1S with 0.4 mm nozzle, 0.20 mm layers, 15% infill and two walls. All three saved plates report no supports. Estimated print time totals **7 h 13 min 57 s**. The saved process preset is named `0.20mm Standard @BBL X1C`; the selected printer profile is P1S.

At Josh’s **approximately $14/kg refill assumption**, material is **296.56/1000 × $14 = $4.15**. The official US store refill comparison checked October 30, 2026 was $14.99/kg, or $4.45 for this mass; this is separate from Josh’s $14/kg default. This is an estimate for this selected printed set, including the torque-test lever. It excludes failed iterations, hardware, shipping, tax and electricity. The $4.15 uses Josh’s approximate paid rate, not today’s listed price. It is not a whole-project cost.

## Geometry and provenance

The STLs were extracted from `cycloidal-actuator-v1-project.3mf`, saved from the current Bambu Studio project on October 30, 2026. All 26 object identities, names and plate assignments match the earlier sliced Full Assembly file. Nested 3MF component references and transforms were resolved before extraction. The manifest records each source object, transform, quantity, bounds and SHA256.

All exported meshes have finite coordinates, closed two-manifold edge incidence, consistent edge winding, positive signed volume and no degenerate triangles. Self-intersections were not tested. No mesh repairs were applied. The 3MF is a mesh-based print project, not a parametric Fusion design or a mechanically assembled model.

This is the printed set. Purchased bearings, steel rods, fasteners, motor, coupler, electronics and wiring are not model downloads. Their precise as-built specifications must be confirmed separately.

## Download privacy

A designer account ID was removed from the downloadable 3MF metadata. Mesh data, component/build transforms, plate settings and every other ZIP member payload are unchanged. No printer connection credentials were found. The source project is preserved separately.
