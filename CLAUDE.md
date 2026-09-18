# desarollo_web_3

Proyecto de desarrollo web en equipo. Cada persona/equipo trabaja en su propia rama.

## Estructura de ramas

- `main` / `master` — solo para entregas finales
- `nombre_apellido` — rama personal de cada integrante (ej. `alejandro_espinosa`)
- `equipo_modulo` — rama por equipo al arrancar cada módulo

## Stack

- **Base de datos:** MongoDB (via Docker)
- **Infraestructura:** Docker Compose

## Levantar el entorno

```bash
docker-compose up -d
```

MongoDB queda disponible en `localhost:27017`.

Credenciales de MongoDB:
- Usuario: `admin_user`
- Contraseña: `web3`

## Estructura del proyecto

```
backend/          # Código del servidor (pendiente de implementar)
mongo_data/       # Datos persistentes de MongoDB (no commitear)
docker-compose.yml
```

## Notas importantes

- `mongo_data/` contiene archivos de runtime de MongoDB — no incluir en commits.
- El backend aún no tiene código; el directorio está vacío esperando implementación.

## Ponerse al día con la rama del profesor

- `sergio_mendoza` es la rama de referencia del profesor: ahí va marcando el avance de la clase.
- Cada alumno debe sincronizar su rama personal contra `sergio_mendoza` de vez en cuando para no atrasarse:
  ```bash
  git fetch origin
  git merge origin/sergio_mendoza -X theirs
  ```
- `-X theirs` resuelve cualquier conflicto de línea aceptando la versión de la rama que se está fusionando (`sergio_mendoza`), en vez del trabajo propio. Úsalo cuando quieras priorizar ponerte al día sobre conservar tus propios cambios en las líneas en conflicto.
- Si el merge es un fast-forward (tu rama no tiene commits propios que no estén ya en `sergio_mendoza`), no hay conflictos que resolver.
