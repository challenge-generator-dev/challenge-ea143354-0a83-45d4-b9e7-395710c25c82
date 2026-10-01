# Desarrollo de una API REST en el dominio de banca

La empresa 'Banco Digital' necesita una API REST que gestione las transacciones de los clientes. La API debe permitir la creación, lectura, actualización y eliminación de transacciones, así como la autenticación de usuarios mediante JWT. Los actores involucrados son el 'cliente', el'sistema de transacciones' y el'motor de autenticación'. Las transacciones tienen propiedades como 'monto', 'fecha', 'descripción' y 'estado'. La API debe garantizar la idempotencia de las solicitudes de creación de transacciones y manejar adecuadamente los errores de autenticación y validación de datos. Se espera un throughput de 1 000 transacciones por segundo en hora pico.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python FastAPI |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de endpoints y autenticación

**Objetivo:** Definir los endpoints de la API y asegurar la autenticación de los usuarios.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Identificar los endpoints necesarios para crear, leer, actualizar y eliminar transacciones.
- Implementar la autenticación de usuarios utilizando JWT.
- Asegurar que los endpoints estén protegidos y solo sean accesibles para usuarios autenticados.

**Entregable:** Documentación de los endpoints y la implementación de la autenticación JWT.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los métodos HTTP apropiados para cada operación.
- Piensa en cómo manejar los tokens de autenticación en las solicitudes y respuestas.

</details>

### Fase 2: Implementación de la lógica de negocio

**Objetivo:** Implementar la lógica de negocio para la gestión de transacciones.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear las funciones para manejar la creación, lectura, actualización y eliminación de transacciones.
- Asegurar la idempotencia de las solicitudes de creación de transacciones.
- Manejar los errores de validación de datos y autenticación.

**Entregable:** Implementación de la lógica de negocio para la gestión de transacciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo garantizar la idempotencia en las solicitudes de creación de transacciones.
- Piensa en cómo manejar los errores de validación y autenticación de forma adecuada.

</details>

### Fase 3: Integración y pruebas

**Objetivo:** Integrar los componentes y realizar pruebas exhaustivas de la API.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Integrar los endpoints y la lógica de negocio.
- Realizar pruebas unitarias y de integración para asegurar la funcionalidad correcta de la API.
- Asegurar que la API cumple con los requisitos de throughput y latencia.

**Entregable:** API REST completamente funcional y documentada.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo integrar los componentes de forma efectiva.
- Piensa en cómo realizar pruebas exhaustivas para asegurar la calidad de la API.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los endpoints de una API y cuál es su propósito en este reto?
- **paraQueSirve**: ¿Para qué sirve la autenticación JWT en este contexto?
- **comoSeUsa**: ¿Cómo se usa la idempotencia en las solicitudes de creación de transacciones?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir durante la validación de datos y autenticación?
- **queDecisionesImplica**: ¿Qué decisiones implica la integración de los componentes y la realización de pruebas exhaustivas?

## Criterios de Evaluacion

- Definición correcta de los endpoints y autenticación JWT.
- Implementación adecuada de la lógica de negocio con idempotencia y manejo de errores.
- Integración efectiva de los componentes y realización de pruebas exhaustivas.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
