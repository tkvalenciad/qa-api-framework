# QA API Framework

Framework de pruebas automatizadas de API en Python, diseñado para validar endpoints REST de forma estructurada y reproducible. 
Utiliza [JSONPlaceholder](https://jsonplaceholder.typicode.com) como API de prueba y se integra con **GitHub Actions** para ejecutar las pruebas en cada push y pull request.

## Características

- Capa de abstracción por recurso (`UserAPI`, `PostAPI`)
- Pruebas organizadas con **pytest** y markers `smoke` / `regression`
- Fixtures compartidas para reutilizar clientes y datos
- Pipeline CI/CD con GitHub Actions
- Reportes HTML locales con `pytest-html`
- URL base configurable mediante variables de entorno

## Estructura del proyecto

```
qa-api-framework/
├── api/
│   ├── config.py       # Configuración y URL base
│   ├── user_api.py     # Endpoints de usuarios (CRUD + posts)
│   └── post_api.py     # Endpoints de posts
├── tests/
│   ├── conftest.py             # Fixtures compartidas
│   ├── test_users.py           # Pruebas de usuarios
│   ├── test_users_negative.py  # Casos negativos (404, IDs inválidos)
│   └── test_posts.py           # Pruebas de posts
├── .github/workflows/
│   └── tests.yml       # Pipeline de GitHub Actions
├── pytest.ini          # Configuración de pytest y markers
└── requirements.txt    # Dependencias del proyecto
```

## Requisitos

- Python 3.12+
- pip

## Instalación

```bash
git clone https://github.com/tkvalenciad/qa-api-framework.git
cd qa-api-framework
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

## Ejecutar pruebas

### Todas las pruebas

```bash
pytest
```

### Solo smoke tests (validación rápida)

```bash
pytest -m smoke
```

### Solo regression tests (cobertura ampliada)

```bash
pytest -m regression
```

### Generar reporte HTML

```bash
pytest -m regression --html=report.html
```

## Suite de pruebas

| Archivo | Descripción | Tests |
|---------|-------------|-------|
| `test_users.py` | Listado, detalle, CRUD, validación de datos y posts por usuario | 14 |
| `test_users_negative.py` | IDs inexistentes e inválidos (404) | 3 |
| `test_posts.py` | Listado, detalle, filtro por usuario y casos negativos | 5 |

**Total: 22 pruebas** (4 smoke, 18 regression)

## GitHub Actions

El workflow `.github/workflows/tests.yml` se ejecuta automáticamente en cada **push** y **pull request** a la rama principal.

### Pasos del pipeline

1. Checkout del código
2. Configuración de Python 3.12
3. Instalación de dependencias (`requirements.txt`)
4. Ejecución de smoke tests (`pytest -m smoke`)
5. Ejecución de regression tests (`pytest -m regression`)

Si alguna suite falla, el pipeline se marca como fallido y el PR no debería fusionarse hasta corregir los errores.

## Configuración

Puedes cambiar la URL base de la API creando un archivo `.env` en la raíz del proyecto:

```env
API_BASE_URL=https://jsonplaceholder.typicode.com
```

Si no se define, se usa JSONPlaceholder por defecto.

## Tecnologías

- [Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/)
- [requests](https://requests.readthedocs.io/)
- [pytest-html](https://pytest-html.readthedocs.io/)
- [GitHub Actions](https://github.com/features/actions)

## Autor

**tkvalenciad**

## Licencia

Este proyecto es de uso educativo y de práctica en automatización de pruebas de API.
