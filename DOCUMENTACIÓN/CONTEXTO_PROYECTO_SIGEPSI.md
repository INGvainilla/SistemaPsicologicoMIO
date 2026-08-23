# PLATAFORMA WEB Y MÓVIL DE GESTIÓN INTEGRAL DE CITAS, EXPEDIENTES CLÍNICOS Y SEGUIMIENTO TERAPÉUTICO PARA CENTROS DE SALUD MENTAL (SIGEPSI)

> Documento de contexto de proyecto — transcripción íntegra y minuciosa del perfil de proyecto "GRUPO_9_Sistema_Psicologico". Este archivo servirá como base de contexto para la construcción del proyecto.

**Universidad Autónoma Gabriel René Moreno**
**Facultad de Ingeniería en Ciencias de la Computación y Telecomunicaciones**

**Grupo # 9**

**Integrantes:**

| Integrante | Registro |
|---|---|
| Condori Diaz Marilyn Esther | 224051237 |
| Delgado Rojas Alberto Caleb | 224027204 |
| Larrazabal Rojas Julio Cesar | 223049255 |
| Mujica Vallejos Andy Mauricio | 224028367 |
| Romero Saavedra Maria Ilse | 222009772 |
| Velasco Soliz Rolando | 223044768 |

---

## ÍNDICE ORIGINAL DEL DOCUMENTO

- PERFIL ................................................................. 6
- 1. INTRODUCCIÓN ......................................................... 6
- 2 ANTECEDENTES ........................................................... 8
  - FUNDAMENTACIÓN TEÓRICA ............................................... 8
  - SISTEMAS SIMILARES .................................................... 9
  - CASOS DE ESTUDIO ...................................................... 10
    - Caso de estudio 1: MentalGest ....................................... 10
    - Caso de estudio 2: Talkspace ........................................ 11
    - Caso de estudio 3: Spring Health .................................... 12
    - Relación de los casos de estudio con el proyecto ..................... 12
- 3 JUSTIFICACIÓN ........................................................... 14
- 4 DESCRIPCIÓN DEL PROBLEMA ............................................... 15
- 5 FORMULACIÓN DEL PROBLEMA .............................................. 20
- 6 OBJETIVOS ............................................................... 21
  - 6.1 Objetivo General .................................................... 21
  - 6.2 Objetivos Específicos ............................................... 21
- 7 ALCANCE .................................................................. 21
  - 7.1 Módulo de Gestión de Usuarios, Roles, Seguridad y Multi-Tenant ..... 22
  - 7.2 Módulo de Panel Administrativo (Dashboard) y Alertas de Priorización 22
  - 7.3 Módulo de Gestión de Psicólogos y Pacientes ......................... 23
  - 7.4 Módulo de Agenda, Citas y Videoconferencias ........................ 23
  - 7.5 Módulo de Historia Clínica, Formulario Previo, Notas y Seguimiento . 24
  - 7.6 Módulo de Aplicación Móvil para Pacientes ........................... 25
  - 7.7 Módulo de Inteligencia Artificial Asistida y Chatbot de Orientación . 25
  - 7.8 Módulo de Reportes Administrativos y Clínicos ....................... 26
  - 7.9 Módulo de Control de Pagos .......................................... 26
  - 7.10 Funcionalidades .................................................... 27
    - 7.10.1 Funcionalidades Web ............................................ 27
    - 7.10.2 Funcionalidades Móvil ........................................... 27
    - 7.10.3 Funcionalidades IA .............................................. 27
- 8 ELEMENTOS DEL SIBC ...................................................... 29
  - 8.1 HARDWARE ............................................................ 29
  - 8.2 SOFTWARE ............................................................ 29
  - 8.3 DATOS ............................................................... 31
  - 8.4 PROCESOS ............................................................ 31
  - 8.5 GENTE / USUARIO ..................................................... 32
  - 8.6 DOCUMENTO ........................................................... 32
- 9 TECNOLOGÍA ............................................................... 33
  - 9.1 Tecnología para el Desarrollo ....................................... 33
  - 9.2 Tecnología para la Puesta en Marcha ................................. 33
- 10 COSTOS PARA LA PUESTA EN MARCHA ....................................... 35
- 11 BENEFICIOS PARA EL CLIENTE ............................................. 37
  - Tiempo ................................................................. 37
  - Esfuerzo Humano ........................................................ 37
  - Costos .................................................................. 38
  - Accesibilidad y Adherencia al Tratamiento .............................. 38
- CAPÍTULO 1 – MARCO TEÓRICO ............................................... 40
  - 1.1 MARCO REFERENCIAL .................................................. 40
    - 1.1.1 Salud Mental .................................................... 40
    - 1.1.2 Psicología Clínica .............................................. 40
    - 1.1.3 Centros Psicológicos y Gabinetes ................................ 40
    - 1.1.4 Historia Clínica Psicológica .................................... 41
    - 1.1.5 Proceso Terapéutico ............................................. 41
    - 1.1.6 Consentimiento Informado en Psicología .......................... 42
    - 1.1.7 Teleconsulta y Telepsicología ................................... 42
    - 1.1.8 Inteligencia Artificial Aplicada a la Salud Mental .............. 42
    - 1.1.9 Modelo SaaS Multi-Tenant ........................................ 43
  - 1.2 MARCO DE TRABAJO ÁGIL SCRUM ........................................ 43
    - 1.2.1 Introducción al Manifiesto Ágil ................................. 43
    - 1.2.2 Los Doce Principios del Manifiesto Ágil ......................... 44
    - 1.2.3 ¿Qué es SCRUM? .................................................. 44
    - 1.2.4 Roles en SCRUM .................................................. 45
    - 1.2.5 Eventos de SCRUM ................................................ 46
    - 1.2.6 Artefactos de SCRUM ............................................. 46
    - 1.2.7 Historias de Usuario ............................................ 47
    - 1.2.8 Aplicación de SCRUM en el Proyecto .............................. 48
- CAPÍTULO 2 – HERRAMIENTAS TECNOLÓGICAS PARA EL DESARROLLO ................ 50
  - 2.1 LENGUAJE DE PROGRAMACIÓN ........................................... 50
  - 2.2 FRAMEWORKS Y ENTORNOS DE EJECUCIÓN ................................. 51
  - 2.3 SISTEMA GESTOR DE BASE DE DATOS .................................... 52
  - 2.4 LENGUAJE DE MODELADO DE SOFTWARE (MODELO C4) ...................... 52
  - 2.5 HERRAMIENTA DE DISEÑO Y MODELADO ................................... 52
  - 2.6 ENTORNO DE DESARROLLO .............................................. 53
  - 2.7 INFRAESTRUCTURA DE SOFTWARE (IaaS) ................................. 53
  - 2.8 HERRAMIENTAS COLABORATIVAS PARA SEGUIMIENTO DE PROYECTOS .......... 54
  - 2.9 SISTEMA DE CONTROL DE VERSIONES DE CÓDIGO (GIT) ................... 54
  - 2.10 HERRAMIENTAS DE GESTIÓN DE CÓDIGO EN LA NUBE ...................... 55
- CAPÍTULO 3 – REQUERIMIENTOS ............................................... 56
  - 3.1 Propósito ........................................................... 56
  - 3.2 Ámbito de Sistema ................................................... 56
  - 3.3 Equipo SCRUM ........................................................ 56
  - 3.4 Definiciones, Acrónimos y Abreviaturas .............................. 57
  - 3.5 Funciones del Producto .............................................. 58
  - 3.6 Product Backlog ..................................................... 60
  - 3.7 Requisitos Funcionales (Elaborar tabla App web y movil) ............ 65
  - 3.8 Requisitos no funcionales ........................................... 72
  - 3.9 Lista de casos de uso (web y móvil) ................................. 74
  - 3.10 Paquetes y casos de Uso ............................................ 76
  - 3.11 Planificación Sprint (Diagrama de Gantt) ........................... 79
- BIBLIÓGRAFA ................................................................ 81
  - a. Libros y Literatura ................................................. 81
  - b. Sitios Web Especializados ........................................... 81
- ANEXOS ..................................................................... 83

---

# PERFIL

## 1. INTRODUCCIÓN

En la actualidad, el uso de herramientas digitales se ha convertido en un elemento fundamental para mejorar la organización y la atención en diferentes áreas de servicio, incluyendo el ámbito de la salud mental. Los centros y gabinetes psicológicos necesitan administrar citas, pacientes, historias clínicas, notas de sesión, pagos, recordatorios y seguimiento de manera ordenada, segura y accesible. Sin embargo, muchos de estos centros realizan sus procesos de forma manual o mediante herramientas dispersas, lo que genera desorganización, pérdida de información y dificultades en la atención al paciente.

El presente perfil de proyecto plantea el desarrollo de una plataforma web y una aplicación móvil basada en un modelo multi-empresa (SaaS Multi-Tenant) para la gestión integral de centros psicológicos. La arquitectura multi-tenant permitirá que múltiples centros, gabinetes o consultorios psicológicos puedan suscribirse e interactuar dentro de la misma solución, manteniendo sus datos, usuarios, horarios y configuraciones completamente aislados y seguros.

La aplicación móvil estará orientada principalmente a los pacientes, facilitando la consulta de citas, notificaciones, llenado de formularios previos a la consulta, interacción con un chatbot de orientación y seguimiento del proceso terapéutico. Por su parte, la plataforma web permitirá al personal administrativo, coordinadores clínicos y psicólogos gestionar de forma completa los pacientes, horarios, expedientes clínicos, sesiones, pagos y reportes consolidados de su respectivo centro.

La finalidad del proyecto es centralizar la información y optimizar los procesos principales de los centros psicológicos mediante una solución tecnológica moderna, escalable y adaptada a las necesidades del área de salud mental, incorporando herramientas de inteligencia artificial asistida bajo supervisión profesional.

Asimismo, la propuesta toma como referencia casos de estudio de plataformas reales como MentalGest, Talkspace y Spring Health, los cuales sirven como antecedentes para identificar funcionalidades, procesos de admisión, matching y buenas prácticas aplicables al desarrollo de esta plataforma.

---

## 2 ANTECEDENTES

Los antecedentes del presente proyecto se organizan en tres partes: la fundamentación teórica que sustenta los conceptos clave del sistema, la identificación de sistemas similares existentes en el mercado y el análisis de tres casos de estudio de plataformas reales relacionadas con la gestión psicológica, la atención virtual y la salud mental digital. Estos elementos permiten comprender qué módulos manejan los sistemas existentes, qué áreas psicológicas atienden y qué funcionalidades pueden servir como referencia para el desarrollo de esta plataforma.

### FUNDAMENTACIÓN TEÓRICA

La fundamentación teórica del presente proyecto se basa en conceptos clave de psicología clínica, gestión en salud mental, modelos SaaS multi-tenant y tecnologías de la información aplicadas al ámbito sanitario.

**Psicología clínica:** La psicología clínica es una rama de la psicología dedicada a la evaluación, diagnóstico, tratamiento y prevención de trastornos mentales y problemas emocionales. Su práctica requiere del registro sistemático de información del paciente, incluyendo antecedentes, motivos de consulta, evolución terapéutica y notas de sesión (American Psychological Association, 2017).

**Historia clínica psicológica:** La historia clínica es el documento médico-legal que contiene la información relevante del paciente, organizada de manera cronológica. En el contexto psicológico, incluye datos personales, antecedentes familiares y personales, motivo de consulta, diagnóstico, plan de tratamiento, notas de sesión y evolución. Su correcta gestión es fundamental para garantizar la continuidad terapéutica y la calidad de atención (Fernández-Ballesteros, 2013).

**Salud mental:** Según la Organización Mundial de la Salud (OMS, 2022), la salud mental es un estado de bienestar en el que la persona puede desarrollar sus capacidades, afrontar el estrés normal de la vida, trabajar productivamente y contribuir a su comunidad. Los centros de atención psicológica cumplen un rol fundamental en la promoción, prevención y tratamiento de problemas de salud mental.

**Proceso terapéutico:** El proceso terapéutico abarca desde la primera consulta hasta el cierre o derivación del caso. Incluye fases de evaluación inicial, establecimiento de objetivos, intervención, seguimiento y evaluación de resultados. Cada fase genera información que debe ser registrada y organizada para garantizar un tratamiento eficaz (Beck, 2011).

**Derivación al psiquiatra:** Cuando el psicólogo identifica que el paciente presenta un cuadro clínico que requiere intervención farmacológica, como depresión severa, ansiedad crónica o trastornos que no responden únicamente a la terapia psicológica, se procede a derivar al psiquiatra. El psiquiatra es el único profesional autorizado para prescribir medicamentos como ansiolíticos o antidepresivos. Esta derivación forma parte del proceso integral de atención y debe quedar registrada en el sistema.

**Consentimiento informado y ética profesional:** El ejercicio de la psicología clínica exige el cumplimiento de principios éticos fundamentales, entre ellos la confidencialidad de la información del paciente, el consentimiento informado para el tratamiento y el manejo responsable de datos sensibles. Estos principios deben reflejarse en cualquier herramienta digital que gestione información clínica (Código de Ética del Psicólogo Boliviano, 2002).

**Arquitectura Multi-Tenant (SaaS):** El modelo de Software como Servicio (SaaS) Multi-Tenant permite atender a múltiples clientes (empresas o centros psicológicos) desde una sola instancia de software, garantizando el aislamiento lógico de los datos de cada centro. Cada entidad suscrita administra sus propios profesionales, horarios, pacientes y finanzas independientemente (Laudon & Laudon, 2020).

**Sistemas de información en salud:** Los sistemas de información en salud son herramientas tecnológicas diseñadas para recopilar, almacenar, gestionar y transmitir información relacionada con la atención sanitaria. En el ámbito psicológico, estos sistemas permiten organizar historias clínicas, agendar citas, generar reportes y facilitar la comunicación entre profesionales y pacientes (Laudon & Laudon, 2020).

**Inteligencia artificial aplicada a la salud mental:** La inteligencia artificial (IA) se ha incorporado progresivamente al ámbito de la salud mental como herramienta de apoyo para la clasificación de casos, detección de patrones de riesgo, generación de resúmenes clínicos y asistencia en la toma de decisiones. En el contexto de la plataforma, se contemplan los siguientes tipos de IA: IA predictiva para la detección temprana de señales de riesgo y patrones de abandono terapéutico, IA generativa para la generación de resúmenes clínicos y notas estructuradas, chatbot conversacional para la orientación inicial del paciente y recopilación de información previa, y sistemas de recomendación para la sugerencia de asignación de pacientes al profesional más adecuado según especialidad, disponibilidad y carga de trabajo. Su uso debe mantenerse siempre bajo supervisión profesional, sin reemplazar el criterio clínico del psicólogo (Graham et al., 2019).

### SISTEMAS SIMILARES

Además de los casos de estudio analizados en detalle, existen otros sistemas y plataformas en el mercado que ofrecen funcionalidades relacionadas con la gestión psicológica y de salud mental. A continuación se presentan algunos sistemas similares que sirven como referencia adicional para el proyecto.

**SimplePractice** (https://www.simplepractice.com/): Plataforma de gestión de consultas de salud con funciones de agenda, notas clínicas, facturación, teletherapy y portal para clientes. Es una de las herramientas más utilizadas por profesionales de salud mental en Estados Unidos. Su enfoque combina gestión administrativa con atención clínica en una sola plataforma.

**TherapyNotes** (https://www.therapynotes.com/): Software de gestión para profesionales de salud mental que incluye notas de tratamiento, agenda, facturación electrónica, portal del paciente y telehealth. Destaca por su enfoque en la documentación clínica estructurada y la facilidad de uso para psicólogos y terapeutas.

Estos sistemas similares complementan la visión obtenida mediante los casos de estudio detallados y permiten identificar funcionalidades estándar de la industria, así como oportunidades de diferenciación para la plataforma en el contexto boliviano.

### CASOS DE ESTUDIO

#### Caso de estudio 1: MentalGest

| Campo | Detalle |
|---|---|
| URL | https://mentalgest.com/ \| https://mentalgest.com/transparencia-ia |
| Tipo de plataforma | Software clínico para psicólogos, consultorios y centros psicológicos. |
| Área principal | Gestión administrativa y clínica psicológica. |

MentalGest es una plataforma digital diseñada para organizar la consulta psicológica en un solo sistema. Integra funciones de agenda, registro de pacientes, historia clínica, notas de sesión, pagos, recordatorios, paquetes de sesiones, reportes e inteligencia artificial asistida.

El flujo inicia cuando el paciente agenda o solicita una cita. Luego el sistema organiza la disponibilidad del profesional, envía recordatorios, permite revisar la ficha del paciente, registrar la sesión, actualizar la evolución y consultar reportes administrativos. La información queda centralizada para que el psicólogo pueda retomar cada caso con mayor contexto.

**Alcance del caso de estudio**
- Gestión de usuarios con roles como profesional y paciente
- Ficha del paciente con datos personales, antecedentes, contacto de emergencia y documentos.
- Historia clínica con notas de sesión, evolución, acuerdos, tareas y próximos pasos.
- Agenda por profesional con reservas, cancelaciones, reprogramaciones e inasistencias.
- Recordatorios automáticos por WhatsApp o correo electrónico.
- Control de pagos, paquetes de sesiones y reportes operativos.
- IA asistida para mejorar notas, resumir casos, transcribir dictados y apoyar el análisis clínico en beneficio para el profesional de la salud mental.

**Áreas psicológicas que puede apoyar**
- Psicología clínica individual.
- Psicoterapia con seguimiento continuo.
- Atención psicológica en centros multiprofesionales.
- Orientación psicológica recurrente.
- Documentación clínica y seguimiento de evolución.

#### Caso de estudio 2: Talkspace

| Campo | Detalle |
|---|---|
| URL | https://www.talkspace.com/ \| Centro de ayuda de Talkspace sobre funcionamiento, matching e intake. |
| Tipo de plataforma | Plataforma de terapia online. |
| Área principal | Atención psicológica virtual y comunicación paciente-profesional. |
| Relación con el proyecto | Sirve como referencia para la aplicación móvil, admisión digital y comunicación con pacientes. |

Talkspace es una plataforma de terapia online que conecta a pacientes con profesionales licenciados de salud mental. Su enfoque está orientado a facilitar el acceso a terapia mediante registro digital, formularios iniciales, asignación de proveedor, mensajería privada y sesiones en vivo.

El paciente se registra, completa un formulario inicial con información sobre su situación y preferencias, y luego la plataforma realiza un proceso de matching con un proveedor adecuado. Después se habilita una sala privada donde el paciente puede comunicarse mediante mensajes o acceder a sesiones en vivo por video, audio o chat.

**Alcance del caso de estudio**
- Registro del paciente desde web o aplicación móvil.
- Formulario de intake para motivo de consulta, antecedentes, objetivos y preferencias.
- Matching con proveedor según necesidad, ubicación, idioma, cobertura y disponibilidad.
- Sala privada de comunicación entre paciente y profesional.
- Mensajería segura para seguimiento entre sesiones.
- Sesiones en vivo por video, audio o chat.
- Cambio de proveedor cuando no existe una buena adaptación terapéutica.

**Especialidades o áreas de salud mental que maneja**
- Terapia individual para adolescentes desde 13 años y adultos.
- Terapia de pareja para dos participantes mayores de 18 años.
- Psiquiatría para adultos, orientada a evaluación psiquiátrica y manejo de medicación.
- Apoyo en ansiedad, estrés, presión académica, relaciones familiares, identidad, tristeza y depresión.
- Atención mediante mensajería y sesiones en vivo según el plan disponible.

#### Caso de estudio 3: Spring Health

| Campo | Detalle |
|---|---|
| URL | https://www.springhealth.com/ \| https://www.springhealth.com/our-approach \| https://www.springhealth.com/what-we-do/springcare |
| Tipo de plataforma | Plataforma de salud mental con evaluación, orientación y derivación. |
| Área principal | Preevaluación, clasificación de necesidad y cuidado personalizado. |

Spring Health es una plataforma de salud mental orientada a conectar a cada usuario con el tipo de atención que necesita. Su enfoque se basa en una evaluación inicial, recomendaciones personalizadas, navegación clínica, matching con proveedores y seguimiento de progreso.

El usuario completa una evaluación breve sobre sus necesidades, síntomas, objetivos y contexto. Con esa información, la plataforma recomienda una ruta de cuidado que puede incluir terapia, coaching, medicación, recursos digitales, atención especializada o apoyo en crisis. La orientación puede estar acompañada por profesionales o navegadores clínicos.

**Alcance del caso de estudio**
- Evaluación inicial para conocer síntomas, objetivos, contexto y necesidades.
- Recomendación de nivel de cuidado según la información recopilada.
- Navegación clínica mediante orientadores o Care Navigators.
- Matching con terapeutas, coaches o profesionales disponibles.
- Terapia virtual o presencial según disponibilidad.
- Coaching para hábitos, productividad, relaciones y crecimiento personal.
- Medicación o psiquiatría cuando el plan lo incluye.
- Recursos digitales de autocuidado y seguimiento entre sesiones.
- Reportes agregados para organizaciones sin exponer información clínica individual.

**Especialidades o áreas de salud mental que maneja**
- Terapia psicológica individual.
- Coaching de bienestar, hábitos y desarrollo personal.
- Medicación o psiquiatría para casos que requieren evaluación farmacológica.
- Atención para niños y adolescentes cuando el beneficio lo permite.
- Apoyo en ansiedad, depresión, estrés, sueño, enfoque y crisis.
- Atención especializada en neurodiversidad, como ADHD, autismo, dislexia u OCD, según disponibilidad.

#### Relación de los casos de estudio con el proyecto

Los tres casos de estudio se complementan entre sí. MentalGest orienta la gestión web y móvil administrativa y clínica de pacientes y profesionales; Talkspace aporta la experiencia móvil del paciente y la atención online mediante video llamadas mediante el rellenado de formulario y asignación de profesional de la salud; y Spring Health permite comprender la preevaluación, clasificación y derivación de casos. A partir de estos referentes, el proyecto plantea una aplicación móvil y una página web para apoyar la gestión administrativa, clínica y de seguimiento de un centro psicológico.

---

## 3 JUSTIFICACIÓN

La selección del presente proyecto responde a la necesidad de contar en Bolivia con una solución digital integrada en la nube (SaaS Multi-Tenant) que permita a múltiples centros, gabinetes y consultorios psicológicos organizar eficientemente sus procesos administrativos, clínicos y de seguimiento.

Actualmente, muchos centros psicológicos operan de forma aislada mediante agendas físicas, hojas de cálculo de Excel, archivos de Word dispersos y coordinación por WhatsApp. Esto provoca desorganización, pérdida de tiempo, duplicidad de datos y falta de continuidad terapéutica.

Desarrollar una plataforma bajo un esquema de suscripción multi-tenant resuelve este problema permitiendo que cualquier centro o profesional independiente se registre, configure su propio espacio de trabajo de manera aislada y acceda a herramientas avanzadas sin requerir infraestructura propia.

La combinación de una plataforma web para la gestión administrativa-clínica del centro y una aplicación móvil orientada al paciente facilitará el agendamiento, el llenado de formularios previos, la realización de teleconsultas, el seguimiento de tareas terapéuticas y el control de pagos. Además, el uso de inteligencia artificial asistida permitirá optimizar el tiempo de los profesionales al sugerir asignaciones de psicólogos, estructurar notas de sesión y generar resúmenes clínicos, siempre bajo la supervisión y validación del criterio profesional.

---

## 4 DESCRIPCIÓN DEL PROBLEMA

La atención en salud mental representa uno de los ámbitos más sensibles y complejos del sistema de salud, ya que involucra no solo el manejo de información administrativa como citas, pagos y horarios, sino también datos clínicos altamente confidenciales que requieren un tratamiento cuidadoso, organizado y seguro. Los centros psicológicos, gabinetes y consultorios que brindan atención en salud mental necesitan gestionar de manera simultánea múltiples procesos: el registro y seguimiento de pacientes, la administración de agendas de profesionales con diferentes especialidades, el control de fichas psicológicas y notas de sesión, la comunicación con los pacientes, el manejo de pagos y la generación de reportes que permitan evaluar el funcionamiento general del centro. Todos estos procesos están interrelacionados y cualquier falla en uno de ellos puede afectar directamente la calidad de la atención que recibe el paciente.

Sin embargo, en el contexto boliviano y en gran parte de Latinoamérica, la realidad de muchos centros psicológicos es que estos procesos se desarrollan de manera manual o mediante herramientas que no están integradas entre sí. Es común encontrar centros que utilizan agendas físicas o cuadernos para organizar las citas, hojas de cálculo en Excel para controlar pagos y asistencia, documentos de Word o archivos en papel para registrar fichas psicológicas y notas de sesión, carpetas digitales separadas en el computador de cada profesional, llamadas telefónicas y mensajes de WhatsApp para coordinar con los pacientes, y formularios impresos que luego deben ser digitalizados o archivados manualmente. Esta dispersión de herramientas y formatos genera un panorama fragmentado donde la información no fluye de manera eficiente entre las diferentes áreas del centro, provocando desorganización, pérdida de datos, duplicidad de registros y dificultades significativas para mantener un seguimiento terapéutico continuo y de calidad.

El problema principal se origina en la ausencia de una solución tecnológica integral, compuesta por una aplicación móvil y una plataforma web, que centralice y conecte los procesos administrativos, clínicos y de comunicación del centro psicológico. La falta de esta herramienta provoca que cada área del centro trabaje de forma aislada e independiente: la administración maneja citas y pagos en sus propios registros, los psicólogos documentan las sesiones y el progreso de sus pacientes en archivos personales que no se comparten con el resto del equipo, los coordinadores clínicos no tienen visibilidad en tiempo real sobre la carga de trabajo de cada profesional ni sobre los casos que requieren atención prioritaria, y los pacientes reciben avisos, indicaciones y recordatorios por canales externos que no guardan relación con el sistema del centro. Como resultado, la información no siempre se encuentra actualizada, disponible ni relacionada entre sí, lo que impacta directamente en la eficiencia operativa del centro y en la experiencia tanto del profesional como del paciente.

A continuación se describen las dimensiones específicas que componen esta problemática:

**1. Ausencia de un sistema integrado para la gestión del centro psicológico**

La primera y más fundamental dimensión del problema corresponde a la inexistencia de una plataforma centralizada que unifique la información del centro psicológico en un solo lugar. Actualmente, los datos de pacientes, horarios de profesionales, registros de pagos, fichas psicológicas, notas de sesión, evolución terapéutica, consentimientos informados, reportes operativos y comunicaciones con pacientes pueden encontrarse distribuidos en múltiples medios físicos y digitales sin conexión entre ellos. Esta fragmentación genera consecuencias graves para el funcionamiento del centro: el personal administrativo no puede verificar en tiempo real si un paciente tiene pagos pendientes al momento de agendar una nueva cita, el psicólogo no tiene acceso inmediato al historial completo del paciente cuando lo necesita, y el coordinador clínico no puede supervisar de manera eficiente la distribución de casos entre los profesionales. La duplicidad de datos se convierte en un problema recurrente, ya que la misma información del paciente puede estar registrada de manera diferente en distintos archivos, generando inconsistencias que dificultan la toma de decisiones y pueden comprometer la calidad de la atención. Además, la pérdida de tiempo en la búsqueda de registros dispersos representa un costo operativo significativo que se acumula día tras día.

**2. Gestión manual de citas, horarios e inasistencias**

La organización de citas constituye una de las actividades más críticas y frecuentes en un centro psicológico, ya que de ella depende el flujo diario de atención y la productividad de los profesionales. Cuando este proceso se realiza de manera manual, utilizando agendas físicas, cuadernos o incluso hojas de cálculo, se incrementa significativamente la probabilidad de errores que afectan tanto al centro como a los pacientes. Los cruces de horarios son un problema frecuente: dos pacientes pueden quedar agendados a la misma hora con el mismo profesional, generando situaciones incómodas y pérdida de confianza. Los olvidos de confirmación provocan que pacientes asistan sin que el profesional esté preparado, o que el profesional espere a un paciente que no confirmó su asistencia. Las reprogramaciones que no se registran correctamente generan confusión sobre las fechas reales de las citas, y las inasistencias que no reciben seguimiento representan una pérdida económica para el centro y un riesgo clínico para el paciente que abandona su proceso sin notificación. La ausencia de recordatorios automáticos agrava esta situación, ya que obliga al personal administrativo a dedicar tiempo considerable a contactar manualmente a cada paciente por teléfono o WhatsApp para confirmar su asistencia, una tarea repetitiva que consume recursos humanos que podrían destinarse a actividades de mayor valor.

**3. Falta de una historia clínica psicológica organizada**

Desde el área clínica, el psicólogo necesita contar con información clara, completa y fácilmente accesible sobre cada uno de sus pacientes: antecedentes personales y familiares, motivo de consulta original, diagnóstico provisional o confirmado, plan de tratamiento establecido, evolución observada a lo largo de las sesiones, acuerdos terapéuticos, tareas asignadas al paciente, observaciones relevantes de sesiones anteriores y cualquier señal de riesgo identificada durante el proceso. Cuando estos datos se registran en documentos separados, en diferentes formatos o de manera no estructurada, se genera una serie de problemas que impactan directamente en la calidad de la atención. El psicólogo pierde tiempo valioso buscando y revisando archivos antes de cada sesión, lo que reduce el tiempo efectivo de atención. La preparación de la sesión se vuelve deficiente porque no siempre se cuenta con un resumen actualizado del estado del paciente. La continuidad terapéutica se ve comprometida porque las notas de sesiones anteriores pueden estar incompletas, ilegibles o dispersas en diferentes ubicaciones. En casos donde un paciente necesita ser atendido por otro profesional del centro, ya sea por vacaciones, licencia médica o derivación, la transferencia de información clínica se vuelve extremadamente difícil si no existe un sistema centralizado que organice el historial completo del caso. Esta situación es particularmente grave en pacientes recurrentes o con procesos de atención prolongados que abarcan meses o incluso años de seguimiento.

**4. Comunicación limitada con el paciente**

La falta de una aplicación móvil dedicada limita severamente la comunicación directa y organizada entre el centro psicológico y sus pacientes. En la práctica actual, los recordatorios de citas, avisos de cambios de horario, solicitudes de información, formularios iniciales, confirmaciones de asistencia e indicaciones post-sesión suelen manejarse a través de canales externos como WhatsApp, llamadas telefónicas, correos electrónicos personales o incluso mensajes de texto, todos ellos medios que no están integrados con los registros del centro y que no garantizan la confidencialidad que requiere la información relacionada con la salud mental. Esta situación reduce significativamente el control que el centro tiene sobre la información transmitida y recibida, ya que los mensajes pueden perderse, no ser leídos o confundirse con comunicaciones personales del paciente. Además, el paciente no cuenta con un medio propio, seguro y dedicado para consultar sus próximas citas, revisar las tareas o indicaciones dadas por su psicólogo, completar formularios previos a la consulta de manera ordenada, acceder a enlaces de videoconferencia o verificar el estado de sus pagos. Esta carencia afecta la experiencia del usuario, reduce su compromiso con el proceso terapéutico y genera una percepción de desorganización que puede influir negativamente en la relación terapéutica y en la imagen profesional del centro.

**5. Escasa generación de reportes para la toma de decisiones**

Otro problema de gran relevancia es la dificultad o imposibilidad práctica de generar reportes consolidados sobre el funcionamiento del centro psicológico. Sin un sistema que recopile y organice la información de manera automática, el centro no puede obtener datos precisos y actualizados sobre indicadores fundamentales como: el número de pacientes activos, nuevos, derivados o que abandonaron el proceso; las citas atendidas versus las inasistencias y cancelaciones; los pagos realizados y pendientes; la carga de trabajo real de cada profesional o tipo de consulta; la demanda por especialidad o tipo de consulta; la evolución general de los casos en tratamiento; y las alertas de riesgo o abandono que requieren atención prioritaria. Sin esta información, la dirección del centro y el coordinador clínico no pueden tomar decisiones informadas sobre la contratación de nuevos profesionales, la reorganización de horarios, la implementación de estrategias para reducir inasistencias, la identificación de áreas que requieren más recursos o la evaluación del impacto general de los servicios que se ofrecen. La ausencia de reportes también dificulta la rendición de cuentas ante instancias reguladoras o institucionales y limita la capacidad del centro para demostrar la efectividad de sus intervenciones.

**6. Necesidad de apoyo tecnológico e inteligencia artificial asistida**

El volumen creciente de información clínica y administrativa que se genera en un centro psicológico activo puede superar la capacidad del personal para procesarla, organizarla y utilizarla de manera eficiente. Los psicólogos dedican una parte considerable de su tiempo a tareas documentales como redactar notas de sesión, actualizar fichas, preparar resúmenes de evolución y revisar antecedentes antes de cada consulta. Los coordinadores clínicos enfrentan el desafío de revisar manualmente los formularios de nuevos pacientes para determinar qué profesional es el más adecuado para cada caso, considerando especialidad, carga de trabajo y características del paciente. El personal administrativo debe compilar información de diferentes fuentes para generar reportes básicos que, en muchos casos, quedan desactualizados antes de ser completados. Ante este panorama, se identifica una necesidad clara de contar con herramientas de apoyo tecnológico, particularmente basadas en inteligencia artificial, que permitan automatizar tareas repetitivas, organizar y resumir información clínica, generar alertas ante situaciones de riesgo, sugerir asignaciones de pacientes a profesionales y facilitar la preparación de sesiones. La inteligencia artificial asistida puede contribuir significativamente en estas tareas, siempre y cuando su uso se mantenga estrictamente bajo validación y supervisión profesional, sin sustituir en ningún caso el criterio clínico del psicólogo ni realizar diagnósticos de manera autónoma.

**7. Falta de personalización y adaptación del proceso terapéutico**

Una dimensión adicional del problema es la dificultad para personalizar y adaptar el proceso terapéutico a las necesidades específicas de cada paciente cuando no se cuenta con un sistema que integre toda la información relevante. Sin una plataforma que permita visualizar de manera clara la evolución del paciente a lo largo del tiempo, comparar el estado inicial con el progreso alcanzado, identificar patrones de comportamiento o asistencia, y registrar de manera estructurada los indicadores de avance, estancamiento o retroceso, el psicólogo debe confiar únicamente en su memoria y en notas dispersas para ajustar el plan de tratamiento. Esta limitación puede provocar que cambios importantes en el estado del paciente pasen desapercibidos, que las intervenciones no se adapten oportunamente a las nuevas necesidades identificadas, y que el proceso terapéutico pierda eficacia por falta de una visión integral y actualizada del caso.

En conclusión, la problemática que enfrentan los centros psicológicos al no contar con una solución tecnológica integrada puede sintetizarse en siete dimensiones principales estrechamente interrelacionadas: la ausencia de un sistema centralizado que unifique la información, la gestión manual e ineficiente de citas y horarios, la falta de una historia clínica organizada y accesible, la comunicación limitada y fragmentada con el paciente, la escasa capacidad de generación de reportes para la toma de decisiones, la necesidad de apoyo tecnológico e inteligencia artificial para optimizar procesos, y la dificultad para personalizar y adaptar el seguimiento terapéutico. Cada una de estas dimensiones no solo representa un problema individual, sino que se retroalimenta con las demás, creando un ciclo de ineficiencia que afecta la calidad de la atención, la satisfacción del paciente, la productividad del profesional y la sostenibilidad operativa del centro. El desarrollo de una aplicación móvil y una plataforma web busca responder de manera integral a estas dificultades mediante una solución digital centralizada, segura, ordenada y específicamente orientada a las necesidades del ámbito de la gestión psicológica y la salud mental.

---

## 5 FORMULACIÓN DEL PROBLEMA

El presente proyecto busca resolver la problemática administrativa, clínica y de seguimiento que presentan los centros psicológicos al no contar con una solución digital para Bolivia, integrada para organizar sus procesos principales. La ausencia de una aplicación móvil y una página web centralizada provoca que la información de pacientes, citas, fichas psicológicas, notas de sesión, pagos, recordatorios y reportes se maneje de forma dispersa, generando desorden, duplicidad de datos, pérdida de información y dificultad para mantener la continuidad del proceso terapéutico.

Para responder a esta problemática, el sistema contemplará módulos de gestión de usuarios y roles, registro de pacientes, ficha psicológica inicial, agenda de citas, recordatorios, notas de sesión, seguimiento terapéutico, control de pagos, reportes básicos, formularios iniciales para pacientes y apoyo mediante inteligencia artificial asistida. La página web estará orientada principalmente al personal administrativo y a los psicólogos, permitiendo gestionar la información del centro de manera ordenada; mientras que la aplicación móvil estará enfocada en facilitar al paciente el acceso a citas, notificaciones, formularios y seguimiento básico.

El desarrollo del proyecto permitirá centralizar la información, mejorar la organización interna, reducir la carga manual del personal, fortalecer la comunicación con los pacientes y apoyar el trabajo clínico del psicólogo mediante herramientas digitales. La inteligencia artificial se utilizará únicamente como apoyo para resumir información, organizar notas y facilitar la revisión de antecedentes, sin reemplazar el criterio profesional ni realizar diagnósticos automáticos.

---

## 6 OBJETIVOS

### 6.1 Objetivo General

Desarrollar una plataforma web y móvil de gestión integral de citas, expedientes clínicos y seguimiento terapéutico para centros de salud mental, basada en un modelo multi-empresa (SaaS Multi-Tenant) con apoyo de inteligencia artificial asistida bajo supervisión profesional.

### 6.2 Objetivos Específicos

- Recolectar información sobre los procesos administrativos, clínicos y de atención al paciente que realizan los centros psicológicos mediante entrevistas, observación y análisis de casos de estudio.
- Analizar los requerimientos funcionales y no funcionales del sistema a partir de la información recolectada para definir los módulos y funcionalidades de la plataforma.
- Diseñar la arquitectura multi-tenant, las interfaces de usuario web y móvil, y el modelo de base de datos que soporte la gestión aislada y segura de múltiples centros.
- Desarrollar la plataforma web para la gestión de usuarios, roles, agenda, expedientes clínicos, notas de sesión, pagos, alertas y reportes del centro.
- Desarrollar la aplicación móvil orientada al paciente para la consulta de citas, formularios previos, notificaciones, seguimiento terapéutico y teleconsulta.
- Implementar módulos de inteligencia artificial asistida para la clasificación de casos, sugerencia de asignación de profesionales, generación de resúmenes clínicos, chatbot de orientación y detección de señales de riesgo.
- Probar las funcionalidades implementadas mediante pruebas de validación e incorporar las correcciones y modificaciones necesarias.

---

## 7 ALCANCE

El alcance del proyecto contempla el desarrollo de una solución basada en una arquitectura de software como servicio multi-empresa (SaaS Multi-Tenant), compuesta por una plataforma web administrativa/clínica y una aplicación móvil orientada a pacientes.

La arquitectura multi-tenant permitirá a múltiples centros, gabinetes o consultorios psicológicos suscribirse e interactuar de forma independiente en la solución, garantizando el aislamiento lógico de la información, usuarios, pacientes y finanzas de cada centro.

La plataforma web estará destinada al personal operativo e interno de los centros psicológicos suscritos: Administradores de Plataforma (SuperAdmin), Administradores de Centro, Recepcionistas, Coordinadores Clínicos y Psicólogos. La aplicación móvil estará orientada principalmente al paciente, facilitando su interacción con el centro, la gestión de sus citas y su seguimiento terapéutico.

A continuación, se describen de manera detallada los 9 módulos consolidados que estructuran el alcance del proyecto:

### 7.1 Módulo de Gestión de Usuarios, Roles, Seguridad y Multi-Tenant

Este módulo constituye el núcleo de control de acceso y seguridad de la plataforma. Diseñado bajo una arquitectura multi-empresa (SaaS Multi-Tenant), permite administrar de forma independiente múltiples centros psicológicos, gabinetes y consultorios privados dentro de una misma solución tecnológica. Cada centro suscrito opera dentro de un entorno aislado con su propia configuración institucional, usuarios, permisos y datos.

- **SuperAdministrador (Plataforma):** Gestiona la plataforma global, da de alta o baja centros psicológicos suscritos (tenants), administra planes de servicio, licencias y supervisa el estado del sistema.
- **Administrador del Centro:** Gestiona la configuración general de su centro específico, alta de personal (recepcionistas, coordinadores, psicólogos), roles institucionales, asignación de permisos y parámetros del gabinete.
- **Recepcionista:** Registra pacientes, agenda citas, confirma asistencia y consulta estados de cuenta básicos.
- **Coordinador Clínico:** Revisa solicitudes de admisión, aprueba o modifica asignaciones de pacientes sugeridas por IA, supervisa derivaciones y atiende alertas de priorización.
- **Psicólogo:** Accede exclusivamente a sus pacientes asignados, agenda personal, fichas clínicas, notas de sesión y seguimiento de casos.
- **Paciente:** Accede a través de la aplicación móvil para revisar sus citas, completar formularios previa consulta, interactuar con el chatbot y recibir indicaciones.
- **Gestión de Permisos y Consentimientos Informados Digitales:** Formalización digital del consentimiento informado para atención psicológica, tratamiento de datos sensibles de salud mental, modalidad de teleconsulta y aceptación de clasificación asistida por IA.
- **Registro de Auditoría e Historial de Accesos:** Trazabilidad completa de accesos, modificaciones de registros y acciones sensibles para garantizar estándares de seguridad y confidencialidad.

### 7.2 Módulo de Panel Administrativo (Dashboard) y Alertas de Priorización

Este módulo actúa como el centro de control operativo de la plataforma web. Permite a los administradores y coordinadores clínicos visualizar en tiempo real la dinámica del centro psicológico, supervisar el flujo de atención y actuar rápidamente ante situaciones críticas.

- **Dashboard Principal e Indicadores Clave (KPIs):** Resumen visual con métricas diarias sobre citas programadas, atendidas, inasistencias, cancelaciones, pacientes activos, nuevos ingresos y porcentaje de ocupación horaria por profesional.
- **Consola de Alertas de Priorización:** Identificación y listado inteligente de casos que requieren atención inmediata, tales como inasistencias consecutivas sin justificación, riesgo de abandono del tratamiento, señales de riesgo detectadas en formularios iniciales o check-ins, y estancamiento o retroceso reportado por el psicólogo en las notas de sesión.
- **Panel de Gestión y Validación del Coordinador Clínico:** Interfaz donde el coordinador clínico puede revisar cada alerta generada, asignar acciones de seguimiento (contacto telefónico, reprogramación, revisión del caso o derivación) y registrar la resolución de la alerta.

### 7.3 Módulo de Gestión de Psicólogos y Pacientes

Este módulo centraliza la administración del talento humano y la gestión de expedientes de los pacientes pertenecientes a cada centro psicológico suscrito. Garantiza que la información clínica y personal esté organizada, actualizada y accesible únicamente para los profesionales autorizados.

- **Perfil Profesional del Psicólogo:** Registro de datos del profesional, número de colegiatura, especialidades (psicología clínica, infantil, adolescente, pareja, familiar, neuropsicología, trauma, etc.), experiencia, modalidad de atención (presencial, virtual o mixta), disponibilidad horaria y cupos máximos de atención.
- **Control de Carga de Trabajo:** Monitoreo continuo de la cantidad de pacientes activos por profesional para evitar sobrecarga de trabajo y asegurar una atención de calidad.
- **Expediente Centralizado del Paciente:** Registro de datos personales, contacto de emergencia, historial de asistencia, profesional asignado y estado del proceso (nuevo, en evaluación, en tratamiento, derivado, inactivo o cerrado).
- **Criterios y Reglas de Asignación:** Vinculación de pacientes con psicólogos basada en especialidad requerida, disponibilidad de agenda, modalidad de atención solicitada y carga actual del profesional.

### 7.4 Módulo de Agenda, Citas y Videoconferencias

Este módulo optimiza la gestión del tiempo y la coordinación diaria entre pacientes, recepcionistas y profesionales de la salud mental. Ofrece herramientas flexibles para la programación de consultas presenciales y la integración de sesiones virtuales.

- **Calendario Interactivo Multivista:** Vista diaria, semanal y mensual por psicólogo, especialidad o sede del centro psicológico, permitiendo la visualización clara de horarios disponibles y bloqueados.
- **Gestión Integral de Citas:** Funciones de reserva, confirmación, cancelación, reprogramación y cambio de estados de cita (pendiente, confirmada, atendida, cancelada, reprogramada e inasistencia).
- **Sistema de Recordatorios Automáticos:** Envío de avisos y confirmaciones de cita a través de notificaciones push en la aplicación móvil y mensajes por correo electrónico para reducir la tasa de inasistencia.
- **Módulo de Teleconsulta y Videoconferencias:** Generación automática de salas virtuales seguras (vía integración con Jitsi Meet / Zoom SDK), registro de enlaces en el sistema, control de accesos para paciente y psicólogo, y registro de asistencia a la sesión remota.

### 7.5 Módulo de Historia Clínica, Formulario Previo, Notas y Seguimiento

Este módulo constituye el núcleo clínico del sistema. Proporciona al psicólogo un marco estructurado y seguro para documentar el proceso terapéutico del paciente, desde la primera toma de contacto hasta el cierre del caso.

- **Formulario Previo a la Consulta (Intake Digital):** Cuestionario estructurado que recopila motivo principal de consulta, síntomas actuales, nivel de urgencia percibido por el paciente, antecedentes relevantes, disponibilidad y preferencias de atención previo a la primera cita.
- **Ficha Psicología Inicial e Historia Clínica:** Documentación cronológica legal del caso con antecedentes personales, familiares, diagnóstico provisional/confirmado y plan de tratamiento establecido.
- **Registro de Notas de Sesión:** Plantilla estructurada para el registro rápido de observaciones post-sesión, avances, intervenciones realizadas y aspectos relevantes del paciente.
- **Registro de Evolución y Seguimiento Terapéutico:** Registro periódico de la evolución clínica del paciente (avance, estancamiento o retroceso), establecimiento de acuerdos terapéuticos, asignación de tareas inter-sesiones e historial comparativo a lo largo del tiempo.
- **Cierre y Derivación del Caso:** Protocolo para el registro del alta terapéutica, pausa del tratamiento o derivación interna/externa (incluyendo derivación al psiquiatra cuando se requiera intervención farmacológica).

### 7.6 Módulo de Aplicación Móvil para Pacientes

La aplicación móvil (desarrollada en Flutter para Android e iOS) actúa como el canal nativo y seguro de interacción del paciente con el centro psicológico. Está enfocada en mejorar la experiencia del usuario, facilitar el autocuidado organizado y fortalecer el compromiso terapéutico.

- **Registro e Inicio de Sesión Seguro:** Autenticación del paciente con protección de datos personales.
- **Gestión de Citas Móvil:** Consulta de próximas citas programadas, historial de atenciones pasadas y solicitud de reprogramación según políticas del centro.
- **Notificaciones Push y Recordatorios:** Recepción de alertas sobre próximas sesiones, formularios pendientes por llenar o tareas asignadas por el psicólogo.
- **Llenado del Formulario Previo:** Interfaz paso a paso para completar el cuestionario inicial de síntomas y motivo de atención antes de la primera cita.
- **Acceso a Teleconsulta:** Enlace directo para ingresar a la sala de videoconferencia segura desde el teléfono móvil a la hora agendada.
- **Portal de Seguimiento y Tareas:** Visualización de indicaciones, acuerdos, tareas asignadas por su terapeuta y registro opcional de check-ins de estado de ánimo.

### 7.7 Módulo de Inteligencia Artificial Asistida y Chatbot de Orientación

La inteligencia artificial en la plataforma actúa exclusivamente como una herramienta de soporte operativo, clínico y documental. No realiza diagnósticos autónomos ni sustituye en ningún caso el criterio profesional del psicólogo.

- **Chatbot Conversacional de Orientación (Recepción Virtual):** Componente conversacional que atiende a los usuarios las 24 horas, responde preguntas frecuentes sobre servicios y horarios, guía al paciente en el llenado del formulario previo y canaliza solicitudes administrativas.
- **Clasificación Inteligente de Motivos de Consulta:** Análisis de procesamiento de lenguaje natural (NLP) sobre las respuestas del formulario previo para clasificar el caso en categorías (ansiedad, depresión, estrés, pareja, orientación vocacional, etc.).
- **Sugerencia de Asignación Asistida:** Algoritmo de recomendación que analiza el perfil del paciente y sugiere al psicólogo o especialista más adecuado del centro según especialidad, disponibilidad y carga horaria (sujeto a aprobación del coordinador clínico).
- **Generación Asistida de Resúmenes Clínicos:** Síntesis generativa que compila notas anteriores y antecedentes del paciente para facilitar la preparación rápida de la sesión por parte del psicólogo.
- **Detección de Señales de Riesgo y Alertas Prioritarias:** Algoritmo que analiza textos en formularios y notas para identificar palabras clave asociadas a situaciones de riesgo elevado o abandono, notificando inmediatamente al coordinador clínico para su revisión.

### 7.8 Módulo de Reportes Administrativos y Clínicos

Este módulo proporciona a la dirección del centro psicológico y al coordinador clínico herramientas de Business Intelligence (BI) para analizar el rendimiento del centro, evaluar la demanda y tomar decisiones informadas sobre la gestión operativa y clínica.

- **Reportes Operativos de Citas y Asistencia:** Estadísticas comparativas de citas programadas, atendidas, inasistencias y cancelaciones por periodo, psicólogo y sede.
- **Reportes de Gestión de Pacientes:** Indicadores sobre volumen de pacientes activos, nuevos ingresos, tasa de deserción, casos cerrados y derivados.
- **Reportes de Demanda por Especialidad:** Análisis de las áreas de atención psicológica más solicitadas para orientar la contratación o formación de profesionales.
- **Reportes de Carga de Trabajo Profesional:** Medición del número de horas clínicas y cantidad de pacientes atendidos por cada psicólogo.
- **Reportes de Evolución y Efectividad Clínica:** Indicadores agregados sobre la tasa de evolución favorable en los pacientes y efectividad de los canales de admisión (chatbot y formularios).
- **Exportación de Datos:** Capacidad para exportar reportes en formatos estándar (PDF, Excel) para respaldos o presentaciones institucionales.

### 7.9 Módulo de Control de Pagos

Este módulo permite gestionar y registrar las transacciones económicas asociadas a los servicios brindados por el centro psicológico, manteniendo un control claro de las cuentas sin reemplazar un sistema contable complejo.

- **Registro de Cobros por Servicio:** Registro de pagos individuales por consulta presencial o virtual, paquetes de sesiones o evaluaciones especiales.
- **Estado de Cuenta del Paciente:** Historial transparente de pagos realizados, saldos pendientes y detalle de montos cobrados por sesión.
- **Control de Métodos de Pago:** Registro del medio de pago utilizado (efectivo, transferencia bancaria, QR o pasarela externa).
- **Historial Financiero Administrativo:** Consulta de ingresos generados por periodo, psicólogo o tipo de servicio, accesible únicamente para el rol administrativo.

### 7.10 Funcionalidades

#### 7.10.1 Funcionalidades Web

La plataforma web está orientada al personal del centro psicológico: administradores de plataforma (SuperAdmin), administradores de centro, recepcionistas, coordinadores clínicos y psicólogos. Permite la gestión centralizada de toda la información administrativa, clínica y multi-tenant de cada centro psicológico suscrito.

- Gestión de Usuarios, Roles, Seguridad y Multi-Tenant
- Panel de Control (Dashboard)
- Gestión de Psicólogos y Especialidades
- Gestión de Pacientes
- Formulario Previo a la Consulta
- Agenda, Citas y Videoconferencias
- Historial Clínico, Notas y Evolución del Paciente
- Alertas para la Priorización y Apoyo a Decisiones
- Reportes Administrativos y Clínicos
- Control de Pagos y Facturación
- Permisos, Consentimientos y Documentación

#### 7.10.2 Funcionalidades Móvil

La aplicación móvil está orientada a mejorar la experiencia del paciente y facilitar su comunicación con el centro. Es el canal principal de interacción entre el paciente y la plataforma.

- Registro e Inicio de Sesión de Pacientes
- Gestión de Citas
- Formulario Previo a la Consulta
- Notificaciones y Recordatorios al Paciente
- Chatbot de Orientación al Paciente
- Seguimiento, Videoconferencias y Tareas Terapéuticas

#### 7.10.3 Funcionalidades IA

La inteligencia artificial en la plataforma se utiliza exclusivamente como herramienta de apoyo para optimizar procesos administrativos y clínicos, siempre bajo supervisión y validación humana. No realiza diagnósticos ni toma decisiones clínicas de manera autónoma.

- Clasificación y Asignación Inicial
- Sugerencias, Recomendaciones y Resúmenes de Seguimientos
- Detección de Señales de Prioridad y Riesgo
- Apoyo a la Toma de Decisiones
- Restricciones Éticas y de Seguridad

---

## 8 ELEMENTOS DEL SIBC

El Sistema de Información Basado en Computadora (SIBC) del proyecto SIGEPSI está compuesto por los siguientes elementos fundamentales:

### 8.1 HARDWARE

**Servidor**
- Servidor en la nube (AWS, DigitalOcean, Railway o equivalente) para el alojamiento de la plataforma web, la API REST del backend y la base de datos del sistema SIGEPSI.
- Sistema operativo del servidor: Linux Ubuntu Server o equivalente, con soporte para despliegue de aplicaciones Django y servicios de base de datos PostgreSQL.
- Capacidad de procesamiento y almacenamiento escalable para soportar el crecimiento del centro psicológico en número de pacientes, profesionales y volumen de datos clínicos.

**Cliente**
- Computadoras de escritorio o portátiles para el personal administrativo, coordinadores clínicos y psicólogos del centro, utilizadas para acceder a la plataforma web administrativa a través de navegadores web modernos.
- Dispositivos móviles (smartphones y tablets) con sistema operativo Android o iOS para el uso de la aplicación móvil por parte de pacientes y profesionales.

**Otros Dispositivos**
- Impresora multifuncional para la generación de reportes impresos, consentimientos informados, fichas y documentación complementaria cuando el centro lo requiera.
- Cámaras web y micrófonos integrados o externos en las computadoras de los psicólogos para la realización de videoconferencias y sesiones virtuales con pacientes.
- Router o punto de acceso inalámbrico para garantizar la conectividad a Internet dentro de las instalaciones del centro psicológico.

### 8.2 SOFTWARE

**Servidor**
- Sistema operativo del servidor: Linux Ubuntu Server o distribución equivalente.
- Framework backend: Django / Django REST Framework (Python). Framework robusto para el desarrollo de la API REST y la lógica de negocio del sistema, con ORM integrado, sistema de autenticación, permisos por roles y generación de endpoints para la comunicación con el frontend web y la aplicación móvil.
- Motor de base de datos relacional: PostgreSQL. Base de datos centralizada que almacenará toda la información del sistema.
- Servidor de aplicación: Gunicorn + Nginx. Servidor WSGI para ejecutar la aplicación Django con proxy reverso para el manejo eficiente de conexiones y servicio de archivos estáticos.
- Motor de inteligencia artificial: API de IA / Modelos de lenguaje (LLM). Servicio de inteligencia artificial para clasificación de texto, generación de resúmenes clínicos, chatbot conversacional y detección de señales de riesgo.

**Cliente**
- Framework frontend web: Angular (TypeScript). Framework de desarrollo web para la construcción de la plataforma administrativa con componentes reutilizables, routing integrado, formularios reactivos y comunicación con la API REST del backend.
- Framework de desarrollo móvil: Flutter (Dart). Framework multiplataforma para el desarrollo de la aplicación móvil del paciente, permitiendo generar aplicaciones nativas para Android e iOS a partir de una sola base de código con alto rendimiento y diseño personalizado.
- Navegadores web modernos (Google Chrome, Mozilla Firefox, Microsoft Edge) para el acceso a la plataforma web administrativa por parte del personal del centro.
- Sistema operativo móvil Android e iOS para la ejecución de la aplicación móvil del paciente desarrollada en Flutter.

**Otro Software Adicional**
- Git / GitHub para el control de versiones del código fuente, colaboración en equipo y trazabilidad de cambios durante el desarrollo.
- Visual Studio Code como IDE de desarrollo con extensiones para Python, TypeScript, Angular, Dart y Flutter.
- Figma para el diseño colaborativo de interfaces, prototipos y experiencia de usuario.
- Jira / Trello para la gestión del proyecto, planificación de sprints, asignación de tareas y seguimiento de avance.
- Postman para pruebas y documentación de la API REST del backend.
- Firebase Cloud Messaging (FCM) para el envío de notificaciones push a la aplicación móvil.
- SendGrid / Mailgun para el envío de correos electrónicos de recordatorios, notificaciones y comunicaciones del sistema.
- Jitsi Meet API / Zoom SDK para la integración de videollamadas en sesiones virtuales.
- Let's Encrypt para la generación de certificados SSL gratuitos que garanticen comunicaciones seguras (HTTPS).

### 8.3 DATOS

Base de datos relacional centralizada en PostgreSQL que almacenará la información de pacientes, psicólogos, especialidades, citas, fichas psicológicas, notas de sesión, evolución terapéutica, pagos, alertas, reportes, consentimientos informados, interacciones con el chatbot y registros de acceso al sistema.

Respaldo periódico y automatizado de la base de datos para garantizar la integridad, disponibilidad y recuperación de la información ante posibles fallos o incidentes.

Encriptación de datos sensibles (información clínica, datos personales del paciente, notas de sesión) para cumplir con principios de confidencialidad y protección de datos en el ámbito de salud mental.

Políticas de retención y eliminación de datos conforme a las regulaciones aplicables y a los consentimientos otorgados por los pacientes.

Separación lógica de datos administrativos y datos clínicos para garantizar que el acceso a información sensible esté restringido según el rol del usuario.

### 8.4 PROCESOS

- Procedimiento de registro de nuevo paciente y completado de formulario previo a la consulta.
- Procedimiento de clasificación y asignación de paciente a psicólogo (manual o asistida por IA), con validación obligatoria del coordinador clínico.
- Procedimiento de agendamiento, confirmación, reprogramación y cancelación de citas.
- Procedimiento de registro de notas de sesión, evolución clínica, acuerdos y tareas terapéuticas.
- Procedimiento de generación y revisión de reportes administrativos y clínicos.
- Procedimiento de gestión de consentimientos informados y autorizaciones de tratamiento de datos.
- Procedimiento de respaldo y recuperación de datos del sistema.
- Procedimiento de atención mediante chatbot y escalamiento a revisión humana cuando se detecten situaciones de riesgo.
- Procedimiento de detección, priorización y atención de alertas de riesgo clínico.
- Procedimiento de registro, control y seguimiento de pagos por sesión o paquete de sesiones.
- Procedimiento de derivación de pacientes a otros profesionales o especialistas del centro.

### 8.5 GENTE / USUARIO

- Administrador del sistema: configura el sistema, gestiona usuarios, roles, permisos y supervisa el funcionamiento general de la plataforma.
- Recepcionista: registra pacientes, agenda citas, confirma asistencia, gestiona consultas administrativas y revisa pagos básicos.
- Coordinador clínico: revisa formularios previos, valida asignaciones sugeridas por IA, supervisa derivaciones y atiende alertas de prioridad.
- Psicólogos: acceden a sus pacientes asignados, registran notas de sesión, fichas clínicas, evolución, seguimiento e historial clínico.
- Pacientes: utilizan la aplicación móvil para consultar citas, completar formularios previos, recibir notificaciones, interactuar con el chatbot y acceder a videoconferencias.
- Equipo de soporte técnico: mantiene el sistema, resuelve incidencias técnicas, aplica actualizaciones y monitorea el rendimiento de la plataforma.

### 8.6 DOCUMENTO

- Consentimiento informado para atención psicológica: documento digital que el paciente acepta antes de iniciar el proceso terapéutico.
- Autorización para tratamiento de datos personales y clínicos dentro del sistema, conforme a las regulaciones de protección de datos.
- Permiso para uso de información en clasificación asistida por IA, informando al paciente sobre el alcance y las limitaciones del uso de inteligencia artificial.
- Consentimiento para atención virtual o videoconferencia, cuando la modalidad de atención sea remota.
- Ficha psicológica inicial del paciente con datos personales, antecedentes, motivo de consulta y contacto de emergencia.
- Notas de sesión registradas por el psicólogo después de cada consulta.
- Reportes administrativos y clínicos generados por el sistema (citas, inasistencias, demanda por especialidad, carga por profesional, evolución de casos).
- Historial de pagos y estado de cuenta del paciente.
- Registro de aceptación de documentos con fecha, versión y usuario que aceptó.
- Documentos adjuntos al expediente del paciente cuando corresponda (derivaciones, informes externos, evaluaciones complementarias).

---

## 9 TECNOLOGÍA

### 9.1 Tecnología para el Desarrollo

- Lenguaje backend: Python. Versatilidad, amplio ecosistema de librerías de IA y facilidad de integración.
- Framework backend: Django / Django REST Framework. Framework robusto para desarrollo web con ORM integrado, sistema de autenticación y API REST.
- Lenguaje frontend web: TypeScript. Lenguaje tipado que extiende JavaScript, estándar de la industria para desarrollo de interfaces web interactivas y mantenibles.
- Framework frontend: Angular. Framework completo de desarrollo web con componentes reutilizables, routing integrado, formularios reactivos, inyección de dependencias y amplia comunidad.
- Desarrollo móvil: Flutter (Dart). Framework multiplataforma de alto rendimiento para desarrollo de aplicaciones nativas en Android e iOS con una sola base de código, diseño personalizado y rendimiento nativo.
- Base de datos: PostgreSQL. Base de datos relacional robusta, escalable y con soporte avanzado para JSON.
- Motor de IA: API de IA / Modelos de lenguaje (LLM). Clasificación de texto, generación de resúmenes, chatbot conversacional y detección de patrones de riesgo. Se podrá utilizar cualquier proveedor de IA disponible según las necesidades del proyecto.
- Control de versiones: Git / GitHub. Control de código fuente, colaboración en equipo y trazabilidad de cambios.
- IDE de desarrollo: Visual Studio Code. Editor ligero con extensiones para Python, TypeScript, Angular, Dart y Flutter.
- Diseño de prototipos: Figma. Herramienta colaborativa para diseño de interfaces y prototipos.
- Gestión de proyecto: Jira / Trello. Planificación de sprints, asignación de tareas y seguimiento de avance.
- Documentación: Markdown / Google Docs. Documentación técnica y colaborativa del proyecto.

### 9.2 Tecnología para la Puesta en Marcha

- Hosting web: AWS / DigitalOcean / Railway. Servicios en la nube escalables con soporte para despliegue de aplicaciones web.
- Servidor de aplicación: Gunicorn + Nginx. Servidor WSGI para Django con proxy reverso para manejo de conexiones.
- Almacenamiento de archivos: AWS S3 / Cloudinary. Almacenamiento seguro de documentos, consentimientos y archivos del paciente.
- Dominio web: Registro de dominio (.com / .bo). Acceso público a la plataforma web.
- Certificado SSL: Let's Encrypt. Certificado gratuito para comunicaciones seguras HTTPS.
- Servicio de correo: SendGrid / Mailgun. Envío de correos electrónicos para recordatorios y notificaciones.
- Notificaciones push: Firebase Cloud Messaging (FCM). Notificaciones push para la aplicación móvil Android e iOS.
- Videollamadas: Jitsi Meet API / Zoom SDK. Integración de videollamadas para sesiones virtuales.
- Distribución móvil: Google Play Store / Apple App Store. Publicación y distribución de la aplicación móvil.
- Monitoreo: Sentry / UptimeRobot. Monitoreo de errores y disponibilidad del sistema.

---

## 10 COSTOS PARA LA PUESTA EN MARCHA

Los costos estimados para la puesta en marcha del sistema SIGEPSI se presentan a continuación. Los montos son referenciales y pueden variar según proveedores y condiciones del mercado.

**Hardware**

| Ítem | Cálculo | Subtotal |
|---|---|---|
| Servidor en la nube (plan mensual, primer año) | 12 meses x 25.00 USD | 300.00 USD |
| Computadora de escritorio para administración | 1 unidad x 500.00 USD | 500.00 USD |
| Dispositivo móvil para pruebas (Android) | 1 unidad x 200.00 USD | 200.00 USD |
| Impresora multifuncional | 1 unidad x 150.00 USD | 150.00 USD |
| **Subtotal Hardware** | | **1,150.00 USD** |

**Software**

| Ítem | Cálculo | Subtotal |
|---|---|---|
| Licencia dominio web (.com, anual) | 1 x 12.00 USD | 12.00 USD |
| Certificado SSL (Let's Encrypt) | Gratuito | 0.00 USD |
| API de IA (OpenAI, créditos mensuales, primer año) | 12 meses x 20.00 USD | 240.00 USD |
| Cuenta de desarrollador Google Play | 1 x 25.00 USD | 25.00 USD |
| Cuenta de desarrollador Apple | 1 año x 99.00 USD | 99.00 USD |
| Servicio de correo electrónico (SendGrid, plan gratuito) | Gratuito | 0.00 USD |
| Herramientas de desarrollo (VS Code, Git, Figma) | Gratuitas | 0.00 USD |
| **Subtotal Software** | | **376.00 USD** |

**Comunicaciones**

| Ítem | Cálculo | Subtotal |
|---|---|---|
| Servicio de Internet del centro (mensual, primer año) | 12 meses x 30.00 USD | 360.00 USD |
| Servicio de notificaciones push (Firebase, plan gratuito) | Gratuito | 0.00 USD |
| Servicio de videollamadas (Jitsi Meet, open source) | Gratuito | 0.00 USD |
| **Subtotal Comunicaciones** | | **360.00 USD** |

**Recursos Humanos**

| Ítem | Cálculo | Subtotal |
|---|---|---|
| Desarrollador full-stack | 2 personas x 6 meses x 800.00 USD | 9,600.00 USD |
| Desarrollador móvil | 1 persona x 5 meses x 800.00 USD | 4,000.00 USD |
| Diseñador UI/UX | 1 persona x 3 meses x 600.00 USD | 1,800.00 USD |
| Especialista en IA | 1 persona x 3 meses x 900.00 USD | 2,700.00 USD |
| Tester / QA | 1 persona x 2 meses x 500.00 USD | 1,000.00 USD |
| **Subtotal Recursos Humanos** | | **19,100.00 USD** |

**Logística**

| Ítem | Cálculo | Subtotal |
|---|---|---|
| Transporte para reuniones con el cliente | 20 visitas x 5.00 USD | 100.00 USD |
| Material de oficina y papelería | — | 30.00 USD |
| Capacitación al personal del centro | 2 sesiones x 50.00 USD | 100.00 USD |
| Contingencias e imprevistos (5%) | — | 105.50 USD |
| **Subtotal Logística** | | **335.50 USD** |

### **COSTO TOTAL ESTIMADO PARA LA PUESTA EN MARCHA: 21,321.50 USD**

---

## 11 BENEFICIOS PARA EL CLIENTE

La adopción de este sistema trae beneficios tangibles operativos y clínicos para los centros de salud mental:

### Tiempo

El sistema digital simplifica y automatiza algunos procesos laboriosos:

- **Menos papeleo:** El Registro Médico Electrónico (Módulo 7.10) ayuda a recopilar todo el papeleo en un solo lugar proporcionando acceso instantáneo al historial, notas de progreso y formularios de consentimiento (Módulo 7.12). No hay necesidad de pasar tiempo buscando registros y haciendo copias.
- **Gestión eficiente de citas:** El Módulo de Citas y Videoconferencia (7.8) cuenta con confirmación automática de citas reduciendo los ausentes. Plataformas como Talkspace tienen una comunicación multifacética (chat, video, mensajes) lo que facilita la programación.
- **Automatización de la Clasificación Inicial:** El Módulo de Clasificación y Asignación con Inteligencia Artificial (7.6) hace un pre-estudio de los clientes sin ningún esfuerzo. Por ejemplo, Spring Health realiza un examen a personas con 12 tipos diferentes de enfermedades mentales y crea planes de tratamiento individuales usando Inteligencia Artificial.
- **Generación instantánea de estadísticas:** El Módulo de Reportes (7.13) recopila automáticamente estadísticas sobre la ocupación, el abandono del tratamiento y la eficiencia eliminando los cálculos manuales.

### Esfuerzo Humano

El sistema libera capacidad clínica y administrativa:

- **Alivio de carga para psicólogos:** El Chatbot de Orientación Inicial (Módulo 7.7) responde consultas elementales, enviando únicamente casos que precisan intervención profesional. Esto facilita que los psicólogos se concentren en sesiones terapéuticas más complejas.
- **Disminución de labores administrativas:** El Módulo de Gestión de Pacientes (7.4) y Permisos/Consentimientos (7.12) automatizan la validación de documentos, la recopilación de formularios previos (Módulo 7.5) y las firmas digitales. Así, el personal administrativo emplea menos tiempo en la gestión documental.
- **Seguimiento continuo entre sesiones:** La función "Guide" de Spring Health conserva todo el contexto del paciente, garantizando apoyo entre sesiones, no solamente durante ellas. Tu Módulo de Alertas y Apoyo a Decisiones (7.11) ofrece el mismo beneficio, posibilitando monitorización remota sin añadir carga clínica.
- **Gamificación de adherencia:** El Módulo Móvil (7.9) incorpora mecanismos de refuerzo positivo (badges, progreso visual de hábitos) que incentivan el cumplimiento del tratamiento sin requerir contacto sincrónico adicional.

### Costos

La digitalización minimiza gastos recurrentes y maximiza los ingresos:

- **Infraestructura:** El diseño del Modelo SaaS Multi-tenant suprime la necesidad de servidores físicos locales, disminuyendo la inversión en hardware y mantenimiento.
- **Eliminación de suministros:** Se reduce de manera significativa el uso de papel, carpetas, archivos físicos y sistemas de almacenamiento costosos.
- **Disminución del ausentismo:** Las confirmaciones automáticas y recordatorios por chat/email (integrados en Módulo 7.8) minimizan las ausencias de pacientes, incrementando la tasa de ocupación de psicólogos.
- **Facturación optimizada:** El Módulo de Pagos y Facturación (7.14) integra cobros online, reduce errores en facturación y acelera recupero de ingresos. Empresas usando plataformas IA-nativas de salud mental reportan reducción de 52% en costos totales de reclamaciones de salud mental.

### Accesibilidad y Adherencia al Tratamiento

- **Disponibilidad extendida:** El video/chat integrado permite sesiones asincrónicas o fuera de horario de oficina, adaptándose a pacientes con restricciones de tiempo. La telepsicología mejora la accesibilidad al tratamiento, permitiendo a personas acceso rápido y fácil a terapias especializadas.
- **Monitoreo continuo:** La App Móvil (7.9) con gamificación y alertas permite que pacientes reporten síntomas, hábitos y estados emocionales entre sesiones. Esto proporciona data clínica más rica y detección temprana de descompensaciones.
- **Mejora de resultados clínicos:** El 92% de miembros usando plataformas IA-First mostraron mejora clínicamente significativa en depresión y ansiedad, recuperándose 5.9 semanas más rápido que en competidores. La implementación de IA para el análisis tiene el potencial de replicar esta capacidad.
- **Disminución de estigma:** La opción de chat y formularios digitales crea espacio psicológicamente seguro para pacientes que sienten vergüenza al hablar cara a cara.

---

# CAPÍTULO 1 – MARCO TEÓRICO

## 1.1 MARCO REFERENCIAL

El presente marco referencial expone los fundamentos, generalidades, características y conceptos específicos del rubro de la salud mental y la gestión de centros psicológicos, los cuales constituyen el dominio principal del sistema a desarrollar.

### 1.1.1 Salud Mental

La Organización Mundial de la Salud (OMS, 2022) define la salud mental como un estado de bienestar en el cual el individuo es consciente de sus propias capacidades, puede afrontar las tensiones normales de la vida, trabajar de forma productiva y fructífera, y es capaz de contribuir a su comunidad. La salud mental no se limita a la ausencia de trastornos mentales, sino que abarca dimensiones emocionales, psicológicas y sociales que influyen en la manera de pensar, sentir y actuar de las personas a lo largo de su vida.

A nivel mundial, los trastornos de salud mental representan una de las principales cargas de enfermedad. Según datos de la OMS, aproximadamente una de cada ocho personas en el mundo padece algún tipo de trastorno mental, siendo los más prevalentes la ansiedad y la depresión. En el contexto latinoamericano y boliviano, el acceso a servicios de salud mental es limitado, lo que incrementa la necesidad de soluciones tecnológicas que faciliten la organización y el alcance de los centros de atención psicológica.

### 1.1.2 Psicología Clínica

La psicología clínica es la rama de la psicología que se ocupa de la investigación, evaluación, diagnóstico, tratamiento, prevención y rehabilitación de los trastornos mentales, emocionales y conductuales. Su práctica profesional requiere del manejo sistemático de información del paciente, incluyendo antecedentes clínicos, evaluaciones psicométricas, diagnósticos, planes de tratamiento y registros de evolución terapéutica (American Psychological Association, 2017).

Los profesionales de la psicología clínica trabajan con diferentes enfoques terapéuticos, entre los que destacan la terapia cognitivo-conductual, la terapia psicodinámica, la terapia humanista, la terapia sistémica y los enfoques integrativos. Cada uno de estos enfoques implica procedimientos específicos de registro y documentación que deben ser contemplados en una plataforma digital de gestión psicológica.

### 1.1.3 Centros Psicológicos y Gabinetes

Un centro psicológico es una institución dedicada a la prestación de servicios de atención en salud mental, que puede contar con uno o varios profesionales especializados en distintas áreas de la psicología. Los centros psicológicos ofrecen servicios como terapia individual, terapia de pareja, terapia familiar, terapia infantil, evaluación psicológica, orientación vocacional, intervención en crisis y programas de prevención.

Un gabinete psicológico es una unidad de atención psicológica que puede estar integrada dentro de una institución educativa, empresarial, hospitalaria o de servicios sociales. El gabinete presta servicios de evaluación, orientación, intervención y derivación, adaptando su oferta a las necesidades específicas de la población que atiende.

Ambos tipos de establecimientos comparten procesos administrativos y clínicos comunes: registro de pacientes, gestión de citas, documentación clínica, control de pagos, coordinación de profesionales y generación de reportes. La sistematización de estos procesos mediante herramientas digitales permite mejorar la eficiencia operativa, la continuidad terapéutica y la calidad de la atención.

### 1.1.4 Historia Clínica Psicológica

La historia clínica psicológica es el documento médico-legal que recopila de manera cronológica y sistemática toda la información relevante del paciente a lo largo de su proceso terapéutico. Constituye un instrumento fundamental para la práctica profesional, ya que garantiza la continuidad de la atención, facilita la comunicación entre profesionales y sirve como respaldo legal del ejercicio profesional (Fernández-Ballesteros, 2013).

Los componentes esenciales de una historia clínica psicológica incluyen: datos de identificación del paciente, motivo de consulta, antecedentes personales (médicos, psicológicos, familiares, académicos, laborales y sociales), evaluación psicológica inicial, diagnóstico (provisional y/o confirmado), plan de tratamiento, notas de sesión, evolución terapéutica, acuerdos y tareas inter-sesiones, consentimiento informado y registro de cierre o derivación del caso.

### 1.1.5 Proceso Terapéutico

El proceso terapéutico en psicología clínica comprende una secuencia estructurada de fases que se desarrollan desde el primer contacto del paciente con el centro hasta el cierre o derivación del caso (Beck, 2011). Las fases principales son:

**Fase de admisión:** El paciente establece el primer contacto con el centro, se registra su información básica, se recopilan datos iniciales sobre el motivo de consulta y se programa la primera cita.

**Fase de evaluación:** El psicólogo realiza una evaluación integral del paciente mediante entrevistas clínicas, observación, aplicación de instrumentos psicométricos y recopilación de antecedentes relevantes. Esta fase culmina con la formulación de un diagnóstico provisional.

**Fase de planificación del tratamiento:** A partir del diagnóstico, se establece un plan de tratamiento con objetivos terapéuticos, estrategias de intervención, frecuencia de sesiones y criterios de evaluación del progreso.

**Fase de intervención:** Se implementan las estrategias terapéuticas planificadas a través de sesiones regulares. Cada sesión se documenta mediante notas que registran las intervenciones realizadas, las observaciones del profesional y el progreso del paciente.

**Fase de seguimiento y evaluación:** Se evalúa periódicamente el avance del paciente respecto a los objetivos planteados, se ajusta el plan de tratamiento según sea necesario y se registra la evolución clínica.

**Fase de cierre o derivación:** Cuando se alcanzan los objetivos terapéuticos, se procede al cierre del caso con un resumen final. Si el paciente requiere atención especializada (por ejemplo, derivación al psiquiatra para intervención farmacológica), se gestiona la derivación correspondiente con toda la documentación necesaria.

### 1.1.6 Consentimiento Informado en Psicología

El consentimiento informado es un requisito ético y legal fundamental en la práctica psicológica. Consiste en un documento mediante el cual el paciente, después de recibir información clara y comprensible sobre el proceso terapéutico, las técnicas a utilizar, los alcances, las limitaciones, la confidencialidad y el tratamiento de sus datos personales, otorga su autorización voluntaria para iniciar el tratamiento (Código de Ética del Psicólogo Boliviano, 2002).

En el contexto de una plataforma digital, el consentimiento informado adquiere dimensiones adicionales: autorización para el almacenamiento y procesamiento electrónico de datos clínicos, consentimiento para el uso de herramientas de inteligencia artificial asistida en la clasificación y organización de información, y autorización para la modalidad de teleconsulta cuando corresponda.

### 1.1.7 Teleconsulta y Telepsicología

La telepsicología se refiere a la prestación de servicios psicológicos a través de tecnologías de telecomunicación, incluyendo videoconferencias, mensajería segura, llamadas telefónicas y plataformas digitales especializadas. Esta modalidad de atención ha experimentado un crecimiento significativo, especialmente tras la pandemia de COVID-19, al permitir el acceso a servicios de salud mental sin las limitaciones geográficas y logísticas de la atención presencial.

La implementación de teleconsulta en un centro psicológico requiere consideraciones técnicas (calidad de la conexión, seguridad de la comunicación, herramientas de videoconferencia), éticas (privacidad del paciente, limitaciones del formato virtual, protocolos de emergencia) y legales (regulación de la práctica a distancia, jurisdicción, consentimiento específico).

### 1.1.8 Inteligencia Artificial Aplicada a la Salud Mental

La inteligencia artificial (IA) se ha incorporado progresivamente al ámbito de la salud mental como herramienta complementaria de apoyo para profesionales. Sus aplicaciones incluyen la clasificación automatizada de texto para identificar patrones en respuestas de pacientes, la generación de resúmenes clínicos a partir de notas de sesión, la detección temprana de señales de riesgo mediante análisis de lenguaje natural y los sistemas de recomendación para la asignación de pacientes a profesionales según criterios de especialidad y disponibilidad (Graham et al., 2019).

Es fundamental establecer que la IA en el contexto de la salud mental opera exclusivamente como herramienta de apoyo y nunca como sustituto del criterio profesional del psicólogo. El sistema no realiza diagnósticos autónomos, no prescribe tratamientos y no toma decisiones clínicas sin la validación y supervisión de un profesional calificado.

### 1.1.9 Modelo SaaS Multi-Tenant

El modelo de Software como Servicio (SaaS) es un modelo de distribución de software en el que las aplicaciones se alojan en la nube y se ofrecen a los usuarios a través de Internet, generalmente bajo un esquema de suscripción. El enfoque multi-tenant (multi-inquilino) permite que una sola instancia del software atienda a múltiples clientes (tenants), donde cada cliente dispone de un entorno lógicamente aislado con sus propios datos, configuraciones y usuarios (Laudon & Laudon, 2020).

En el contexto del proyecto, el modelo SaaS Multi-Tenant permite que múltiples centros psicológicos, gabinetes y consultorios se suscriban a la plataforma y operen de manera independiente dentro de la misma infraestructura tecnológica, garantizando la confidencialidad y el aislamiento de los datos de cada centro. Este modelo reduce significativamente los costos de infraestructura, mantenimiento y actualización para cada centro suscrito.

## 1.2 MARCO DE TRABAJO ÁGIL SCRUM

### 1.2.1 Introducción al Manifiesto Ágil

El desarrollo ágil de software surge como respuesta a las limitaciones de las metodologías tradicionales de desarrollo (cascada, espiral), que presentaban dificultades para adaptarse a los cambios frecuentes en los requisitos y las necesidades del cliente. En el año 2001, un grupo de profesionales del desarrollo de software firmó el Manifiesto por el Desarrollo Ágil de Software, estableciendo cuatro valores fundamentales:

- **Individuos e interacciones sobre procesos y herramientas:** Se prioriza la comunicación directa, la colaboración y el trabajo en equipo por encima de la rigidez de los procesos formales.
- **Software funcionando sobre documentación extensiva:** Se valora la entrega frecuente de software operativo como medida principal de progreso, sin descuidar la documentación necesaria.
- **Colaboración con el cliente sobre negociación contractual:** Se busca una relación continua y colaborativa con el cliente, integrándolo al proceso de desarrollo para asegurar que el producto responda a sus necesidades reales.
- **Respuesta ante el cambio sobre seguir un plan:** Se acepta y gestiona el cambio como parte natural del desarrollo, adaptando los planes en función de las nuevas necesidades identificadas durante el proceso.

### 1.2.2 Los Doce Principios del Manifiesto Ágil

Los doce principios que complementan los valores del manifiesto ágil son:

1. Nuestra mayor prioridad es satisfacer al cliente mediante la entrega temprana y continua de software con valor.
2. Aceptamos que los requisitos cambien, incluso en etapas tardías del desarrollo. Los procesos ágiles aprovechan el cambio para proporcionar ventaja competitiva al cliente.
3. Entregamos software funcional frecuentemente, entre dos semanas y dos meses, con preferencia al periodo de tiempo más corto posible.
4. Los responsables de negocio y los desarrolladores trabajan juntos de forma cotidiana durante todo el proyecto.
5. Los proyectos se desarrollan en torno a individuos motivados. Hay que darles el entorno y el apoyo que necesitan, y confiarles la ejecución del trabajo.
6. El método más eficiente y efectivo de comunicar información al equipo de desarrollo y entre sus miembros es la conversación cara a cara.
7. El software funcionando es la medida principal de progreso.
8. Los procesos ágiles promueven el desarrollo sostenible. Los promotores, desarrolladores y usuarios debemos ser capaces de mantener un ritmo constante de forma indefinida.
9. La atención continua a la excelencia técnica y al buen diseño mejora la agilidad.
10. La simplicidad, o el arte de maximizar la cantidad de trabajo no realizado, es esencial.
11. Las mejores arquitecturas, requisitos y diseños emergen de equipos autoorganizados.
12. A intervalos regulares el equipo reflexiona sobre cómo ser más efectivo para a continuación ajustar y perfeccionar su comportamiento en consecuencia.

### 1.2.3 ¿Qué es SCRUM?

SCRUM es un marco de trabajo ágil liviano que ayuda a las personas, equipos y organizaciones a generar valor a través de soluciones adaptativas para problemas complejos. Se basa en el empirismo y el pensamiento Lean, utilizando un enfoque iterativo e incremental para optimizar la previsibilidad y el control del riesgo.

SCRUM fue concebido inicialmente por Hirotaka Takeuchi e Ikujiro Nonaka en un artículo publicado en 1986 en Harvard Business Review, donde describieron un nuevo enfoque para el desarrollo de productos. Posteriormente, Ken Schwaber y Jeff Sutherland formalizaron SCRUM como marco de trabajo para el desarrollo de software en la década de 1990.

Los tres pilares fundamentales de SCRUM son:

- **Transparencia:** El proceso y el trabajo deben ser visibles para quienes realizan el trabajo y quienes lo reciben. Las decisiones importantes se basan en el estado percibido de sus tres artefactos formales.
- **Inspección:** Los artefactos de SCRUM y el progreso hacia los objetivos acordados deben inspeccionarse de manera frecuente y diligente para detectar variaciones o problemas potencialmente indeseables.
- **Adaptación:** Si algún aspecto de un proceso se desvía fuera de los límites aceptables o si el producto resultante es inaceptable, el proceso que se está aplicando o los materiales que se están produciendo deben ajustarse lo antes posible.

### 1.2.4 Roles en SCRUM

El equipo SCRUM está compuesto por tres roles claramente definidos, cada uno con responsabilidades específicas:

- **Product Owner (Propietario del Producto):** Es la persona responsable de maximizar el valor del producto resultante del trabajo del equipo de desarrollo. Es el responsable de la visión del producto y de las prioridades del backlog. El Product Owner es la única persona autorizada para tomar decisiones sobre las funcionalidades y el orden de prioridad del Product Backlog. Debe conocer profundamente el negocio del cliente y las necesidades de los usuarios. Sus responsabilidades incluyen: definir y comunicar claramente el objetivo del producto, crear y comunicar los elementos del Product Backlog, ordenar los elementos del Product Backlog según prioridad y asegurarse de que el Product Backlog sea transparente, visible y comprensible.
- **Scrum Master (Facilitador):** Es el responsable de establecer SCRUM tal como se define en la Guía de SCRUM. Lo logra ayudando a todos a comprender la teoría y la práctica de SCRUM, tanto dentro del equipo como en la organización. El Scrum Master facilita el proceso, elimina impedimentos que obstaculizan el progreso del equipo, protege al equipo de interferencias externas y asegura que se sigan las prácticas de SCRUM correctamente. Si el equipo falla en un sprint, gran parte de la responsabilidad recae sobre el Scrum Master por no haber sabido lidiar con los obstáculos del equipo.
- **Equipo de Desarrollo (Development Team):** Son los profesionales responsables de crear el incremento del producto en cada sprint. El equipo de desarrollo es autoorganizado, multifuncional y cuenta con todas las habilidades necesarias para crear un incremento de producto. El tamaño óptimo del equipo de desarrollo es de 5 a 9 personas. Menos de 5 personas disminuyen la interacción y resultan en ganancias de productividad menores, mientras que más de 9 miembros requieren demasiada coordinación. Sus responsabilidades incluyen: obtener los requisitos, realizar el análisis, diseño, implementación, pruebas, validaciones y verificaciones, y entregar el 100% de su responsabilidad a través de historias de usuario.

Además de los roles centrales, existen los Stakeholders (partes interesadas): son las personas a las cuales el proyecto les beneficia. No son parte directa del equipo de desarrollo, pero participan durante las revisiones del sprint y proporcionan retroalimentación. Los stakeholders son quienes validan si el producto funciona como la empresa necesita.

### 1.2.5 Eventos de SCRUM

SCRUM define cinco eventos formales que crean regularidad y minimizan la necesidad de reuniones no definidas:

- **Sprint:** Es el corazón de SCRUM. Es un contenedor para todos los demás eventos. Durante el Sprint, se crea un incremento de producto utilizable y potencialmente desplegable. Los Sprints tienen una duración fija (generalmente entre 2 y 4 semanas) y un nuevo Sprint comienza inmediatamente después de la conclusión del Sprint anterior.
- **Planificación del Sprint (Sprint Planning):** Es el evento que inicia cada Sprint. En esta reunión, el equipo SCRUM define qué trabajo puede realizarse durante el Sprint y cómo se llevará a cabo. El resultado principal de la planificación es el Sprint Backlog, que contiene las historias de usuario y tareas seleccionadas para el Sprint.
- **Reunión Diaria (Daily Scrum):** Es una reunión de 15 minutos que se realiza cada día del Sprint. En ella, los miembros del equipo de desarrollo responden tres preguntas clave: ¿Qué hice ayer? ¿Qué haré hoy? ¿Qué impedimentos tengo? Todos los impedimentos identificados deben ser registrados y resueltos por el Scrum Master.
- **Revisión del Sprint (Sprint Review):** Se realiza al final de cada Sprint para inspeccionar el incremento y adaptar el Product Backlog si es necesario. El equipo presenta el trabajo completado a los stakeholders y se recopila retroalimentación.
- **Retrospectiva del Sprint (Sprint Retrospective):** Se realiza después de la Revisión del Sprint y antes de la siguiente Planificación del Sprint. El equipo reflexiona sobre el Sprint pasado, identifica qué salió bien, qué se puede mejorar y establece acciones concretas de mejora para el próximo Sprint.

### 1.2.6 Artefactos de SCRUM

SCRUM utiliza tres artefactos principales que representan trabajo o valor:

- **Product Backlog (Pila del Producto):** Es una lista ordenada y emergente de todo lo que es necesario en el producto. Es la única fuente de requisitos para cualquier cambio a realizarse en el producto. El Product Owner es el responsable de su contenido, disponibilidad y ordenación. El Product Backlog contiene historias de usuario, características, funcionalidades, mejoras y correcciones que constituyen los cambios que se realizarán en el producto en futuras entregas.
- **Sprint Backlog (Pila del Sprint):** Es el conjunto de elementos del Product Backlog seleccionados para el Sprint, junto con un plan para entregar el incremento del producto y cumplir el objetivo del Sprint. Es una previsión realizada por el equipo de desarrollo sobre qué funcionalidad formará parte del próximo incremento y el trabajo necesario para entregar esa funcionalidad.
- **Incremento:** Es la suma de todos los elementos del Product Backlog completados durante un Sprint y el valor de los incrementos de todos los Sprints anteriores. Al final de un Sprint, el nuevo incremento debe estar terminado, lo que significa que debe estar en condiciones de utilizarse.

### 1.2.7 Historias de Usuario

Las historias de usuario son una técnica de especificación de requisitos utilizada en metodologías ágiles. Representan una funcionalidad del sistema desde la perspectiva del usuario final. Su formato estándar es:

> Como [rol de usuario], quiero [funcionalidad/acción], para [beneficio/valor].

Cada historia de usuario debe cumplir con los criterios INVEST: Independiente, Negociable, Valiosa, Estimable, Pequeña (Small) y Comprobable (Testable). Las historias de usuario se descomponen en tareas técnicas que el equipo de desarrollo implementa durante el Sprint. A continuación se presentan las historias de usuario correspondientes al Sprint 0 del proyecto, las cuales abarcan los casos de uso CU1, CU2, CU3 y CU4, y los requisitos funcionales RF-01, RF-02 y RF-03, relacionados con la gestión de usuarios, roles, permisos, autenticación y configuración de la arquitectura Multi-Tenant.

**Historias de Usuario: Sprint 0**

| ID | Título | Rol | Historia de Usuario |
|---|---|---|---|
| HU-01 | Registro de SuperAdministrador | SuperAdmin | Como SuperAdministrador, quiero registrarme con credenciales seguras, para acceder al panel de administración global del sistema. |
| HU-02 | Inicio de sesión multi-rol | Todos los roles | Como usuario del sistema, quiero iniciar sesión con mi correo y contraseña mediante tokens, para acceder a las funcionalidades de mi rol. |
| HU-03 | Alta de centros psicológicos | SuperAdmin | Como SuperAdministrador, quiero dar de alta un nuevo centro psicológico, para que opere con datos aislados. |
| HU-04 | Configuración del centro | Admin de Centro | Como Administrador del Centro, quiero configurar los datos institucionales, para personalizar el funcionamiento de la plataforma. |
| HU-05 | Registro de usuarios del centro | Admin de Centro | Como Administrador del Centro, quiero registrar usuarios dentro de mi centro, para que accedan al sistema. |
| HU-06 | Asignación de roles y permisos | Admin de Centro | Como Administrador del Centro, quiero asignar roles y permisos, para controlar el acceso de cada persona. |
| HU-07 | Aislamiento Multi-Tenant | Admin de Centro | Como Administrador del Centro, quiero que mi información esté aislada de otros centros, para garantizar la confidencialidad. |
| HU-08 | Gestión de centros suscritos | SuperAdmin | Como SuperAdministrador, quiero editar, suspender o dar de baja centros, para mantener el control de la plataforma. |
| HU-09 | Cierre de sesión seguro | Todos los roles | Como usuario del sistema, quiero cerrar mi sesión de manera segura, para proteger mi cuenta. |
| HU-10 | Recuperación de contraseña | Todos los roles | Como usuario del sistema, quiero recuperar mi contraseña por correo, para acceder si olvidé mis credenciales. |

### 1.2.8 Aplicación de SCRUM en el Proyecto

Para el presente proyecto, se aplicará el marco de trabajo SCRUM de la siguiente manera:

Se conformará un equipo SCRUM con los roles de Product Owner, Scrum Master y Equipo de Desarrollo distribuidos entre los integrantes del grupo.

El desarrollo se organizará en un Sprint 0 (preparación e infraestructura inicial) seguido de 4 Sprints de desarrollo incremental, con las siguientes fechas de presentación:

- **Sprint 0:** 25 y 27 de agosto de 2026
- **Sprint 1:** 08 y 10 de septiembre de 2026
- **Sprint 2:** 06 y 08 de octubre de 2026
- **Sprint 3:** 03 y 05 de noviembre de 2026

Se elaborará un Product Backlog con todas las funcionalidades identificadas en el alcance del proyecto, priorizadas según el valor para el cliente y la complejidad técnica. Para cada Sprint se seleccionarán las historias de usuario correspondientes, conformando el Sprint Backlog respectivo.

El Sprint 0 contemplará la configuración inicial del entorno de desarrollo, la implementación del módulo de gestión de usuarios (login, roles y permisos) y la preparación de la infraestructura base del proyecto.

> **Nota:** El documento original menciona 4 Sprints de desarrollo incremental con 4 fechas de presentación (Sprint 0 a Sprint 3), aunque en el Product Backlog y la planificación Gantt (secciones 3.6 a 3.11) se detallan tareas hasta Sprint 4 (SP4). Se transcribe tal cual figura en el documento original, incluyendo esta aparente inconsistencia, para no omitir información.

---

# CAPÍTULO 2 – HERRAMIENTAS TECNOLÓGICAS PARA EL DESARROLLO

El presente capítulo describe de manera detallada las herramientas tecnológicas seleccionadas para el desarrollo del proyecto, justificando su elección en función de los requerimientos técnicos, la escalabilidad, el rendimiento y la compatibilidad con la arquitectura propuesta.

## 2.1 LENGUAJE DE PROGRAMACIÓN

### 2.1.1 Python (Backend)

Python es un lenguaje de programación de alto nivel, interpretado, de tipado dinámico y multiparadigma (soporta programación orientada a objetos, funcional e imperativa). Fue creado por Guido van Rossum y su primera versión fue publicada en 1991. Python se caracteriza por su sintaxis clara y legible, su amplio ecosistema de librerías y frameworks, y su comunidad activa a nivel mundial.

En el contexto del proyecto, Python se utiliza como lenguaje principal para el desarrollo del backend (servidor) de la plataforma web. Su elección se justifica por las siguientes razones: amplio ecosistema de librerías para inteligencia artificial y procesamiento de lenguaje natural (TensorFlow, PyTorch, NLTK, spaCy, Hugging Face), frameworks robustos para desarrollo web (Django, FastAPI), excelente soporte para APIs RESTful, facilidad de integración con bases de datos relacionales y servicios en la nube, y comunidad activa con documentación extensa.

Versión recomendada: Python 3.11 o superior.

### 2.1.2 TypeScript (Frontend Web)

TypeScript es un lenguaje de programación desarrollado por Microsoft que extiende JavaScript añadiendo tipado estático opcional, interfaces, enumeraciones y otras características que mejoran la mantenibilidad y la escalabilidad de las aplicaciones web. TypeScript se compila a JavaScript estándar, lo que garantiza compatibilidad con todos los navegadores modernos.

Su uso en el proyecto se justifica por la detección temprana de errores en tiempo de compilación, el autocompletado inteligente y la navegación de código en el IDE, la mejora de la documentación implícita a través de los tipos y la compatibilidad nativa con el framework Angular.

Versión recomendada: TypeScript 5.x.

### 2.1.3 Dart (Desarrollo Móvil)

Dart es un lenguaje de programación desarrollado por Google, optimizado para la construcción de interfaces de usuario rápidas en cualquier plataforma. Dart es el lenguaje utilizado por el framework Flutter para el desarrollo de aplicaciones móviles multiplataforma. Se caracteriza por su compilación AOT (Ahead-of-Time) para producir código nativo de alto rendimiento, su compilación JIT (Just-in-Time) para ciclos de desarrollo rápidos con hot reload, y su sistema de tipos seguro contra nulos (null safety).

Versión recomendada: Dart 3.x (incluido con Flutter SDK).

## 2.2 FRAMEWORKS Y ENTORNOS DE EJECUCIÓN

### 2.2.1 Django / Django REST Framework (Backend Web)

Django REST Framework (DRF) es una extensión de Django que proporciona herramientas para la construcción de APIs RESTful. DRF ofrece serialización de datos, vistas basadas en clases y funciones, autenticación por tokens (JWT), paginación, filtrado, permisos granulares y documentación automática de la API.

En el proyecto, Django y DRF conformarán el backend que expone la API REST consumida tanto por la plataforma web (Angular) como por la aplicación móvil (Flutter).

### 2.2.2 Angular (Frontend Web)

Angular se selecciona para este proyecto por su robustez en aplicaciones empresariales, su tipado fuerte con TypeScript, su arquitectura modular que facilita el mantenimiento y su amplia adopción en la industria.

Versión recomendada: Angular 17 o superior.

### 2.2.3 Flutter (Desarrollo Móvil)

Flutter es un framework de desarrollo de aplicaciones multiplataforma creado por Google. Permite construir aplicaciones nativas para Android e iOS desde una sola base de código en Dart. Flutter utiliza su propio motor de renderizado (Skia), lo que le permite ofrecer alto rendimiento y consistencia visual en todas las plataformas.

Flutter se selecciona para la aplicación móvil orientada al paciente por su capacidad de generar aplicaciones nativas para Android e iOS con una sola base de código, reduciendo tiempos y costos de desarrollo.

Versión recomendada: Flutter 3.x.

## 2.3 SISTEMA GESTOR DE BASE DE DATOS

### 2.3.1 PostgreSQL

En el proyecto, PostgreSQL almacenará toda la información del sistema: usuarios, pacientes, psicólogos, citas, historias clínicas, notas de sesión, pagos, alertas, reportes y configuraciones de cada centro suscrito (tenant). La separación lógica de datos entre tenants se implementará mediante esquemas de PostgreSQL.

Versión recomendada: PostgreSQL 16 o superior.

## 2.4 LENGUAJE DE MODELADO DE SOFTWARE (MODELO C4)

El proyecto utiliza el Modelo C4 como lenguaje de modelado de software para documentar la arquitectura del sistema. El Modelo C4 fue creado por Simon Brown y proporciona un conjunto de abstracciones jerárquicas para describir la arquitectura de software en cuatro niveles de detalle:

- **Nivel 1 (Contexto):** Define la relación entre los usuarios (SuperAdmin, Administrador, Recepcionista, Coordinador, Psicólogo, Paciente), las plataformas (web y móvil) y servicios externos (IA, Firebase, Jitsi Meet, SendGrid, pagos).
- **Nivel 2 (Contenedores):** Desglosa la infraestructura principal en app web (Angular), app móvil (Flutter), API REST (Django/DRF), base de datos (PostgreSQL), IA, notificaciones (Firebase) y videoconferencias (Jitsi Meet).
- **Nivel 3 (Componentes):** Detalla los módulos internos del backend en Django (autenticación, pacientes, agenda, historia clínica, IA, pagos y reportes).
- **Nivel 4 (Código):** Clases e interfaces que se desarrollarán paulatinamente durante los sprints.

## 2.5 HERRAMIENTA DE DISEÑO Y MODELADO

### 2.5.1 Figma

Figma es una herramienta de diseño de interfaces colaborativa basada en la nube. Permite a los equipos de diseño y desarrollo crear prototipos interactivos, wireframes y diseños de alta fidelidad de manera simultánea. Se utiliza en el proyecto para diseñar las interfaces de usuario de la plataforma web y la aplicación móvil, crear sistemas de diseño con componentes reutilizables, desarrollar prototipos interactivos para validación con usuarios y documentar guías de estilo y patrones de interfaz.

### 2.5.2 Enterprise Architect / Herramientas UML

Para el modelado de software, se utilizarán herramientas que soporten la notación UML y el Modelo C4, tales como Enterprise Architect, StarUML, Draw.io o Structurizr (específico para diagramas C4). Estas herramientas permiten crear y mantener los diagramas de arquitectura, casos de uso, secuencia, clases y demás artefactos de modelado requeridos durante el desarrollo del proyecto.

## 2.6 ENTORNO DE DESARROLLO

### 2.6.1 Visual Studio Code

Visual Studio Code (VS Code) es un editor de código fuente ligero, multiplataforma y altamente extensible desarrollado por Microsoft. Es el entorno de desarrollo principal del proyecto gracias a su amplio ecosistema de extensiones.

Extensiones utilizadas en el proyecto: Python (soporte para linting, debugging, IntelliSense y formateo), Angular Language Service (autocompletado y verificación de templates Angular), Dart y Flutter (soporte completo para desarrollo móvil con hot reload), PostgreSQL (conexión y consulta de bases de datos), GitLens (visualización avanzada de historial Git), Prettier (formateo de código), ESLint (análisis estático de código TypeScript) y Thunder Client o REST Client (pruebas de API REST).

## 2.7 INFRAESTRUCTURA DE SOFTWARE (IaaS)

La Infraestructura como Servicio (IaaS) proporciona recursos de computación virtualizados a través de Internet. Para el proyecto se consideran proveedores que ofrecen máquinas virtuales, almacenamiento, redes y otros recursos fundamentales de infraestructura bajo demanda. El servidor en la nube alojará la aplicación Django, la base de datos PostgreSQL y los servicios complementarios del sistema, proporcionando escalabilidad vertical y horizontal según las necesidades de crecimiento del proyecto.

### 2.7.1 SERVICIO EN LA NUBE (CLOUD COMPUTING)

El proyecto utilizará servicios de computación en la nube para el despliegue y operación de la plataforma. El proveedor seleccionado es:

- **Google Cloud Platform (GCP):** Proporciona Compute Engine, Cloud SQL, Cloud Storage, Cloud Functions y servicios avanzados de IA como Vertex AI.

### 2.7.2 SaaS (SOFTWARE AS A SERVICE)

El modelo SaaS (Software como Servicio) es el modelo de distribución adoptado para el proyecto. Bajo este modelo, la plataforma se ofrece como un servicio accesible a través de Internet, donde cada centro psicológico suscrito (tenant) accede a la misma instancia de la aplicación pero opera dentro de un entorno lógicamente aislado.

La implementación del modelo multi-tenant en el proyecto se realizará mediante una de las siguientes estrategias de aislamiento en PostgreSQL:

**Aislamiento por esquema:** Cada tenant dispone de su propio esquema de base de datos dentro de la misma instancia de PostgreSQL. Esta estrategia ofrece un buen equilibrio entre aislamiento de datos y eficiencia de recursos. Se utilizará la librería django-tenants o similar para gestionar la creación automática de esquemas, el enrutamiento de consultas según el tenant y las migraciones compartidas.

Cada centro psicológico suscrito tendrá su propio conjunto de datos completamente aislado: usuarios, pacientes, psicólogos, citas, historias clínicas, pagos y configuraciones. Un SuperAdministrador gestionará la plataforma global, mientras que cada Administrador de Centro gestionará únicamente los datos de su tenant correspondiente.

## 2.8 HERRAMIENTAS COLABORATIVAS PARA SEGUIMIENTO DE PROYECTOS

### 2.8.1 Jira Software

Jira Software es una herramienta de gestión de proyectos ágiles desarrollada por Atlassian. Permite planificar sprints, crear y asignar historias de usuario, rastrear el progreso del desarrollo, generar tableros Kanban y Scrum, y generar reportes de velocidad del equipo. En el proyecto, Jira se utilizará como la herramienta principal para la gestión del Product Backlog, la planificación de sprints y el seguimiento del avance de cada historia de usuario.

## 2.9 SISTEMA DE CONTROL DE VERSIONES DE CÓDIGO (GIT)

Git es un sistema de control de versiones distribuido, creado por Linus Torvalds en 2005. Permite rastrear cambios en el código fuente, colaborar en equipo de manera simultánea, gestionar ramas de desarrollo independientes y mantener un historial completo de todas las modificaciones realizadas.

En el proyecto, se aplicará la siguiente estrategia de ramificación:

- **Rama principal (main):** Contiene el código estable y desplegable en producción.
- **Rama de desarrollo (develop):** Rama de integración donde se fusionan las ramas de características antes de pasar a producción.
- **Ramas de características (feature/nombre):** Cada integrante del equipo trabaja en su propia rama de características. Cuando la funcionalidad está completa y probada, se crea un Pull Request para su revisión y fusión con la rama develop.
- **Ramas de corrección (hotfix/nombre):** Para correcciones urgentes que se aplican directamente sobre la rama principal.

## 2.10 HERRAMIENTAS DE GESTIÓN DE CÓDIGO EN LA NUBE

### 2.10.1 GitHub

GitHub es la plataforma de alojamiento de código basada en Git más utilizada a nivel mundial. Proporciona repositorios remotos, gestión de Pull Requests, revisión de código, GitHub Actions (CI/CD), gestión de issues y wikis de documentación. En el proyecto, GitHub será la plataforma principal para alojar el repositorio del código fuente, gestionar las contribuciones del equipo mediante Pull Requests y automatizar procesos de integración continua.

El repositorio del proyecto se organizará con la siguiente estructura: un repositorio para el backend (Django/DRF), un repositorio para el frontend web (Angular) y un repositorio para la aplicación móvil (Flutter), facilitando la gestión independiente de cada componente del sistema.

---

# CAPÍTULO 3 – REQUERIMIENTOS

## 3.1 Propósito

Este proyecto tiene como propósito desarrollar una **Plataforma Web y Móvil de Gestión Inteligente e Integral de Salud Mental para Centros Psicológicos, Seguimiento de Pacientes y Gestión del Gabinete Psicológico**. La plataforma busca centralizar la información administrativa y clínica de los centros psicológicos, optimizar la gestión de pacientes, profesionales, citas y procesos terapéuticos, mejorar el seguimiento de los casos, facilitar la comunicación con los pacientes y contribuir a una atención más organizada, segura, eficiente y personalizada. Asimismo, incorporará herramientas de inteligencia artificial asistida para apoyar determinados procesos bajo supervisión profesional.

## 3.2 Ámbito de Sistema

El sistema cubrirá los aspectos relacionados con la gestión integral de centros, gabinetes y consultorios psicológicos, abarcando procesos administrativos, clínicos, terapéuticos y de seguimiento. Su alcance comprende desde la administración de centros mediante un modelo SaaS Multi-Tenant, el registro de usuarios, psicólogos y pacientes, la programación de citas, formularios previos, historias clínicas, notas de sesión, evolución terapéutica, videoconferencias y control de pagos, hasta la generación de reportes, alertas de priorización, chatbot de orientación y herramientas de inteligencia artificial asistida. También contará con una aplicación móvil orientada al paciente para facilitar citas, notificaciones, formularios y tareas terapéuticas. No obstante, la plataforma se limitará a procesos propios de la gestión psicológica y administrativa relacionada con la atención del paciente, dejando fuera procesos contables avanzados, diagnóstico autónomo mediante inteligencia artificial y prescripción de medicamentos.

## 3.3 Equipo SCRUM

### 3.3.1 Product Owner

El Product Owner será el responsable de gestionar y priorizar el Product Backlog del proyecto, asegurando que el equipo de desarrollo trabaje en los requerimientos que aporten mayor valor a la plataforma. Su función principal será representar las necesidades del proyecto, establecer prioridades y convertir los objetivos definidos en funcionalidades claras y comprensibles para el equipo. Asimismo, deberá velar porque las funcionalidades desarrolladas respondan a los requerimientos relacionados con usuarios, centros psicológicos, psicólogos, pacientes, agenda, citas, historia clínica, seguimiento terapéutico, aplicación móvil, pagos, reportes, chatbot e inteligencia artificial asistida.

### 3.3.2 Stakeholders

Los Stakeholders son todas aquellas personas, instituciones o entidades interesadas en el desarrollo y resultado del proyecto, aunque no formen parte directa del equipo SCRUM. En este proyecto, los stakeholders estarán conformados principalmente por centros psicológicos, gabinetes, consultorios privados, administradores, recepcionistas, coordinadores clínicos, psicólogos y pacientes que utilizarán o se beneficiarán de la plataforma. Su participación será importante porque permitirán proporcionar necesidades, observaciones y retroalimentación sobre el funcionamiento esperado, contribuyendo a validar que las funcionalidades desarrolladas respondan adecuadamente a los procesos administrativos, clínicos y terapéuticos de un centro psicológico.

### 3.3.3 Scrum Master

El Scrum Master será el facilitador del equipo y tendrá la responsabilidad de asegurar que se apliquen correctamente los principios y prácticas de SCRUM durante el desarrollo del proyecto. Su función consistirá en coordinar y apoyar las reuniones de trabajo, identificar y eliminar impedimentos que puedan afectar el avance del equipo, fomentar una comunicación efectiva entre los integrantes y promover la mejora continua. Además, deberá contribuir a que el equipo mantenga una dinámica organizada, colaborativa y enfocada en el cumplimiento de los objetivos establecidos para cada Sprint durante el desarrollo progresivo de la plataforma web y móvil.

### 3.3.4 Scrum Development

El Scrum Development estará conformado por los integrantes encargados de analizar, diseñar, desarrollar, integrar, probar y validar las diferentes funcionalidades de la plataforma. Será un equipo multidisciplinario y autoorganizado, orientado a entregar incrementos funcionales del producto al finalizar cada Sprint. Dentro de sus responsabilidades se encontrará el desarrollo progresivo de los módulos web, móvil, backend, base de datos e inteligencia artificial, además de las pruebas y documentación correspondiente. De esta manera, el equipo de desarrollo tendrá un rol fundamental en la construcción técnica y funcional de la solución propuesta.

**Conformación del Equipo SCRUM del proyecto:**

| Rol | Integrante(s) |
|---|---|
| PRODUCT OWNER | Condori Diaz Marilyn Esther |
| SCRUM MASTER | Delgado Rojas Alberto Caleb |
| DEVELOPMENT TEAM | Mujica Vallejos Andy Mauricio; Velasco Soliz Rolando; Larrazabal Rojas Julio Cesar; Romero Saavedra Maria Ilse |

## 3.4 Definiciones, Acrónimos y Abreviaturas

- **SaaS (Software as a Service):** Modelo de distribución de software mediante el cual la plataforma se ofrece como un servicio accesible a través de Internet.
- **Multi-Tenant:** Arquitectura que permite que múltiples centros psicológicos utilicen una misma plataforma manteniendo sus datos, usuarios y configuraciones lógicamente aislados.
- **IA (Inteligencia Artificial):** Conjunto de técnicas y tecnologías utilizadas como apoyo para clasificar información, generar resúmenes, identificar señales de riesgo y facilitar determinados procesos del sistema.
- **NLP (Natural Language Processing):** Procesamiento del lenguaje natural utilizado para analizar e interpretar información textual ingresada por los pacientes y usuarios.
- **LLM (Large Language Model):** Modelo de lenguaje utilizado como apoyo para funciones conversacionales, generación de resúmenes y procesamiento de información textual.
- **Sprint:** Período de tiempo definido durante el cual el equipo Scrum desarrolla un conjunto específico de tareas seleccionadas del Product Backlog.
- **CU:** Casos de uso.
- **HU:** Historias de usuario.
- **RF:** Requisitos funcionales.
- **RNF:** Requisitos no funcionales.
- **API (Application Programming Interface):** Interfaz de programación que permite la comunicación entre la plataforma web, la aplicación móvil y los diferentes servicios externos.
- **DB:** Base de datos.
- **UML (Unified Modeling Language):** Lenguaje de modelado utilizado para representar, visualizar y documentar diferentes elementos y procesos del software.
- **BI (Business Intelligence):** Conjunto de herramientas y técnicas utilizadas para analizar información y generar indicadores que apoyen la toma de decisiones.
- **IaaS (Infrastructure as a Service):** Modelo de servicio en la nube utilizado para proporcionar infraestructura tecnológica de forma virtual.
- **SGBD:** Sistema Gestor de Base de Datos utilizado para almacenar, organizar y administrar la información de la plataforma.

## 3.5 Funciones del Producto

Este software cumple con la función de ser una **Plataforma Web y Móvil de Gestión Inteligente e Integral de Salud Mental para Centros Psicológicos, Seguimiento de Pacientes y Gestión del Gabinete Psicológico**, integrando procesos administrativos, clínicos, terapéuticos y de seguimiento dentro de una misma solución tecnológica.

- **Gestión de Usuarios, Roles y Centros Psicológicos:** La plataforma permite registrar y administrar usuarios de acuerdo con diferentes roles y permisos. Mediante su arquitectura SaaS Multi-Tenant, cada centro psicológico podrá gestionar su propia información, profesionales, pacientes y configuraciones en un entorno independiente y seguro.
- **Gestión de Psicólogos y Pacientes:** Permite registrar, actualizar, consultar y organizar la información de psicólogos y pacientes. Los perfiles de profesionales podrán incluir especialidades, disponibilidad, modalidad de atención y carga de trabajo, mientras que cada paciente contará con un expediente centralizado.
- **Gestión de Agenda, Citas y Videoconferencias:** La plataforma permite programar, confirmar, reprogramar y cancelar citas presenciales o virtuales, además de controlar sus diferentes estados. También contempla recordatorios automáticos y acceso a videoconferencias para facilitar las sesiones psicológicas a distancia.
- **Gestión de Historia Clínica Psicológica:** Permite almacenar y consultar antecedentes personales y familiares, motivo de consulta, diagnóstico, plan de tratamiento, notas de sesión, observaciones, evolución terapéutica y demás información necesaria para mantener organizado el proceso clínico del paciente.
- **Gestión de Formularios Previos y Seguimiento Terapéutico:** La plataforma permite recopilar información inicial sobre síntomas, motivo de consulta, nivel de urgencia, antecedentes y preferencias del paciente antes de la primera sesión. Posteriormente permite registrar avances, estancamientos, retrocesos, acuerdos y tareas terapéuticas.
- **Panel Administrativo y Alertas de Priorización:** El sistema proporciona un panel de control con información sobre citas, pacientes, inasistencias, ocupación y otros indicadores relevantes. Además, permite mostrar alertas relacionadas con casos que requieren seguimiento, posibles abandonos o situaciones que necesitan revisión profesional.
- **Chatbot Inteligente de Orientación:** La plataforma incorpora un chatbot conversacional orientado a responder preguntas frecuentes sobre servicios, horarios y funcionamiento del centro, guiar al paciente durante el llenado de formularios y canalizar solicitudes administrativas de manera automática.
- **Clasificación y Asignación Asistida por Inteligencia Artificial:** El sistema permite analizar la información proporcionada por el paciente para clasificar inicialmente el motivo de consulta y sugerir al profesional más adecuado de acuerdo con especialidad, disponibilidad y carga de trabajo, requiriendo siempre validación del coordinador clínico.
- **Generación de Resúmenes y Detección de Señales de Riesgo:** La inteligencia artificial podrá apoyar al psicólogo mediante la generación de resúmenes basados en antecedentes y notas registradas, además de identificar palabras o patrones que puedan requerir atención prioritaria. Estas funciones no reemplazarán el criterio del profesional.
- **Aplicación Móvil para Pacientes:** Permite a los pacientes consultar próximas citas, recibir notificaciones y recordatorios, completar formularios previos, acceder a videoconferencias, revisar tareas asignadas por su psicólogo e interactuar con el chatbot desde un dispositivo móvil.
- **Gestión de Reportes Administrativos y Clínicos:** La plataforma permite generar reportes relacionados con citas atendidas, inasistencias, pacientes activos, nuevos ingresos, carga de trabajo de los profesionales, demanda por especialidad, evolución general de casos y otros indicadores de apoyo para la gestión del centro psicológico.
- **Gestión de Pagos, Consentimientos y Seguridad:** Permite registrar pagos por consultas o servicios, consultar saldos e historiales y controlar los diferentes métodos de pago. También administra consentimientos informados, autorizaciones para el tratamiento de datos, permisos para teleconsulta y registros de auditoría de acciones sensibles.

## 3.6 Product Backlog

| NRO | ID | Rol | Características / Funcionalidad | Tiempo Estimado | Prioridad |
|---|---|---|---|---|---|
| 1 | SP0-1 | Equipo SCRUM | Entrevista con el Product Owner para identificar las necesidades principales del proyecto | 4 hr | Media |
| 2 | SP0-2 | Equipo SCRUM | Crear el perfil que explique la finalidad y características principales del proyecto | 2 hr | Alta |
| 3 | SP0-3 | Equipo SCRUM | Explicar al Product Owner el funcionamiento de la metodología ágil SCRUM | 2 hr | Baja |
| 4 | SP0-4 | Equipo SCRUM | Explicar al equipo la definición y formulación del problema | 5 hr | Alta |
| 5 | SP0-5 | Equipo SCRUM | Realizar la asignación de roles del equipo SCRUM | 1 hr | Media |
| 6 | SP0-6 | Equipo SCRUM | Capacitar a los integrantes en las herramientas y tecnologías que se utilizarán | 3 hr | Alta |
| 7 | SP0-7 | Equipo SCRUM | Preparar el entorno de desarrollo para backend, web, móvil y base de datos | 5 hr | Alta |
| 8 | SP0-8 | Equipo SCRUM | Presentar un prototipo inicial de la plataforma web y aplicación móvil | 6 hr | Media |
| 9 | SP0-9 | Equipo SCRUM | Identificar los casos de uso funcionales de la plataforma web y móvil | 3 hr | Alta |
| 10 | SP0-10 | Equipo SCRUM | Realizar el modelado inicial de la base de datos PostgreSQL | 8 hr | Alta |
| 11 | SP0-11 | Equipo SCRUM | Diseñar la interfaz de inicio de sesión | 2 hr | Alta |
| 12 | SP0-12 | Equipo SCRUM | Implementar el registro, autenticación e inicio de sesión de usuarios | 5 hr | Alta |
| 13 | SP0-13 | Equipo SCRUM | Realizar pruebas del registro e inicio de sesión | 2 hr | Media |
| 14 | SP0-14 | Equipo SCRUM | Diseñar la interfaz para la gestión de usuarios, roles y permisos | 4 hr | Alta |
| 15 | SP0-15 | Equipo SCRUM | Implementar la gestión de usuarios, roles y permisos | 8 hr | Alta |
| 16 | SP0-16 | Equipo SCRUM | Diseñar la configuración de centros psicológicos bajo arquitectura Multi-Tenant | 4 hr | Alta |
| 17 | SP0-17 | Equipo SCRUM | Implementar el aislamiento de información de cada centro psicológico mediante Multi-Tenant | 8 hr | Alta |
| 18 | SP0-18 | Equipo SCRUM | Realizar pruebas de usuarios, roles, permisos y aislamiento Multi-Tenant | 4 hr | Alta |
| 19 | SP1-1 | Equipo SCRUM | Diseñar la interfaz para la gestión de psicólogos y sus perfiles profesionales | 4 hr | Alta |
| 20 | SP1-2 | Equipo SCRUM | Implementar la gestión de psicólogos, especialidades, disponibilidad y modalidad de atención | 8 hr | Alta |
| 21 | SP1-3 | Equipo SCRUM | Realizar pruebas de la gestión de psicólogos | 3 hr | Media |
| 22 | SP1-4 | Equipo SCRUM | Diseñar la interfaz para la gestión de pacientes | 4 hr | Alta |
| 23 | SP1-5 | Equipo SCRUM | Implementar el registro, actualización y consulta de pacientes | 8 hr | Alta |
| 24 | SP1-6 | Equipo SCRUM | Realizar pruebas de la gestión de pacientes | 3 hr | Media |
| 25 | SP1-7 | Equipo SCRUM | Diseñar la interfaz del Dashboard administrativo y clínico | 4 hr | Alta |
| 26 | SP1-8 | Equipo SCRUM | Implementar Dashboard con indicadores de citas, pacientes, inasistencias y carga profesional | 8 hr | Alta |
| 27 | SP1-9 | Equipo SCRUM | Realizar pruebas del Dashboard e indicadores principales | 3 hr | Media |
| 28 | SP1-10 | Equipo SCRUM | Diseñar la interfaz para agenda y gestión de citas | 4 hr | Alta |
| 29 | SP1-11 | Equipo SCRUM | Implementar reserva, confirmación, cancelación y reprogramación de citas | 8 hr | Alta |
| 30 | SP1-12 | Equipo SCRUM | Realizar pruebas de agenda y gestión de citas | 3 hr | Media |
| 31 | SP1-13 | Equipo SCRUM | Diseñar la interfaz para sesiones virtuales y videoconferencias | 3 hr | Media |
| 32 | SP1-14 | Equipo SCRUM | Implementar la integración de videoconferencias mediante Jitsi Meet o Zoom | 7 hr | Alta |
| 33 | SP1-15 | Equipo SCRUM | Realizar pruebas de acceso y funcionamiento de las videoconferencias | 3 hr | Media |
| 34 | SP2-1 | Equipo SCRUM | Diseñar la interfaz del formulario previo a la consulta del paciente | 4 hr | Alta |
| 35 | SP2-2 | Equipo SCRUM | Implementar el formulario previo con motivo de consulta, síntomas, urgencia y antecedentes | 8 hr | Alta |
| 36 | SP2-3 | Equipo SCRUM | Realizar pruebas del formulario previo a la consulta | 3 hr | Media |
| 37 | SP2-4 | Equipo SCRUM | Diseñar la interfaz para la historia clínica psicológica | 4 hr | Alta |
| 38 | SP2-5 | Equipo SCRUM | Implementar la gestión de historia clínica psicológica del paciente | 8 hr | Alta |
| 39 | SP2-6 | Equipo SCRUM | Realizar pruebas de la gestión de historia clínica psicológica | 3 hr | Media |
| 40 | SP2-7 | Equipo SCRUM | Diseñar la interfaz para notas de sesión y evolución terapéutica | 4 hr | Alta |
| 41 | SP2-8 | Equipo SCRUM | Implementar el registro de notas, avances, acuerdos, tareas y evolución del paciente | 8 hr | Alta |
| 42 | SP2-9 | Equipo SCRUM | Realizar pruebas del seguimiento y evolución terapéutica | 3 hr | Media |
| 43 | SP2-10 | Equipo SCRUM | Diseñar la interfaz para consentimientos informados y autorizaciones | 3 hr | Alta |
| 44 | SP2-11 | Equipo SCRUM | Implementar la gestión digital de consentimientos informados y permisos | 6 hr | Alta |
| 45 | SP2-12 | Equipo SCRUM | Realizar pruebas de consentimientos y autorizaciones del paciente | 2 hr | Media |
| 46 | SP2-13 | Equipo SCRUM | Implementar el proceso de cierre, pausa y derivación de casos psicológicos | 6 hr | Alta |
| 47 | SP2-14 | Equipo SCRUM | Realizar pruebas del proceso de cierre y derivación de pacientes | 3 hr | Media |
| 48 | SP3-1 | Equipo SCRUM | Diseñar las interfaces de registro e inicio de sesión de la aplicación móvil | 4 hr | Alta |
| 49 | SP3-2 | Equipo SCRUM | Implementar registro e inicio de sesión de pacientes en la aplicación móvil | 7 hr | Alta |
| 50 | SP3-3 | Equipo SCRUM | Realizar pruebas del registro e inicio de sesión móvil | 3 hr | Media |
| 51 | SP3-4 | Equipo SCRUM | Diseñar la interfaz móvil para gestión de citas y notificaciones | 4 hr | Alta |
| 52 | SP3-5 | Equipo SCRUM | Implementar consulta de citas, recordatorios y notificaciones push | 8 hr | Alta |
| 53 | SP3-6 | Equipo SCRUM | Realizar pruebas de citas y notificaciones en la aplicación móvil | 3 hr | Media |
| 54 | SP3-7 | Equipo SCRUM | Diseñar la interfaz móvil para seguimiento, tareas y videoconferencias | 4 hr | Alta |
| 55 | SP3-8 | Equipo SCRUM | Implementar acceso a tareas terapéuticas, seguimiento y teleconsulta desde la aplicación móvil | 8 hr | Alta |
| 56 | SP3-9 | Equipo SCRUM | Realizar pruebas de seguimiento, tareas y videoconferencias en la aplicación móvil | 3 hr | Media |
| 57 | SP3-10 | Equipo SCRUM | Diseñar la interfaz conversacional del chatbot de orientación | 3 hr | Alta |
| 58 | SP3-11 | Equipo SCRUM | Implementar el chatbot para orientación, consultas frecuentes y apoyo en formularios | 8 hr | Alta |
| 59 | SP3-12 | Equipo SCRUM | Realizar pruebas del chatbot con diferentes consultas de pacientes | 3 hr | Media |
| 60 | SP3-13 | Equipo SCRUM | Implementar la clasificación asistida del motivo de consulta y sugerencia de psicólogo | 8 hr | Alta |
| 61 | SP3-14 | Equipo SCRUM | Realizar pruebas de clasificación y asignación asistida por inteligencia artificial | 4 hr | Alta |
| 62 | SP4-1 | Equipo SCRUM | Diseñar las funciones de inteligencia artificial para resúmenes clínicos y alertas de riesgo | 4 hr | Alta |
| 63 | SP4-2 | Equipo SCRUM | Implementar la generación asistida de resúmenes clínicos | 8 hr | Alta |
| 64 | SP4-3 | Equipo SCRUM | Implementar la detección de señales de riesgo y generación de alertas prioritarias | 8 hr | Alta |
| 65 | SP4-4 | Equipo SCRUM | Realizar pruebas de resúmenes, alertas y restricciones de inteligencia artificial | 4 hr | Alta |
| 66 | SP4-5 | Equipo SCRUM | Diseñar la interfaz para reportes administrativos y clínicos | 4 hr | Alta |
| 67 | SP4-6 | Equipo SCRUM | Implementar reportes de citas, pacientes, inasistencias, demanda y carga profesional | 8 hr | Alta |
| 68 | SP4-7 | Equipo SCRUM | Realizar pruebas y exportación de reportes en PDF y Excel | 4 hr | Media |
| 69 | SP4-8 | Equipo SCRUM | Diseñar la interfaz para el control de pagos y estado de cuenta del paciente | 3 hr | Alta |
| 70 | SP4-9 | Equipo SCRUM | Implementar registro de cobros, saldos pendientes y métodos de pago | 7 hr | Alta |
| 71 | SP4-10 | Equipo SCRUM | Realizar pruebas del módulo de control de pagos | 3 hr | Media |
| 72 | SP4-11 | Equipo SCRUM | Implementar y verificar auditoría de accesos, seguridad y trazabilidad de acciones sensibles | 6 hr | Alta |
| 73 | SP4-12 | Equipo SCRUM | Realizar pruebas finales de integración de la plataforma web, aplicación móvil, IA y base de datos | 8 hr | Alta |

## 3.7 Requisitos Funcionales (Elaborar tabla App web y movil)

| ID | Funcionalidad | Descripción | Módulo | Plataforma | Prioridad |
|---|---|---|---|---|---|
| RF-01 | Registro y autenticación multi-rol | El sistema debe permitir el registro e inicio de sesión de usuarios con roles diferenciados (Super Admin, Admin de Centro, Psicólogo, Paciente) mediante autenticación segura basada en tokens. | Gestión de Usuarios y Roles | Web / Móvil | Alta |
| RF-02 | Gestión de tenants (centros psicológicos) | El sistema debe permitir el alta, configuración y desactivación de centros psicológicos como entidades independientes dentro de la plataforma SaaS. | Gestión de Usuarios y Roles | Web | Alta |
| RF-03 | Asignación de roles y permisos | El sistema debe permitir al administrador de cada centro asignar y modificar roles y permisos a los usuarios de su tenant. | Gestión de Usuarios y Roles | Web | Alta |
| RF-04 | Panel de indicadores administrativos | El sistema debe presentar al administrador métricas operativas del centro (citas realizadas, ocupación de psicólogos, pacientes activos) en tiempo real. | Dashboard Administrativo | Web | Alta |
| RF-05 | Gestión de configuración del centro | El sistema debe permitir personalizar parámetros del tenant (horarios, especialidades ofrecidas, políticas de cancelación). | Dashboard Administrativo | Web | Media |
| RF-06 | Registro de pacientes | El sistema debe permitir el alta de pacientes con validación de datos personales y de contacto en tiempo real. | Gestión de Pacientes | Web / Móvil | Alta |
| RF-07 | Gestión de perfiles de psicólogos | El sistema debe permitir administrar los perfiles profesionales, incluyendo especialidad, formación, tarifas y disponibilidad horaria. | Gestión de Psicólogos | Web | Alta |
| RF-08 | Formulario de pre-consulta | El sistema debe presentar al paciente un formulario estructurado previo a su primera sesión, recabando motivo de consulta y datos clínicos iniciales. | Formularios de Pre-consulta | Web / Móvil | Alta |
| RF-09 | Validación dinámica de formularios | El sistema debe validar en tiempo real los campos del formulario de pre-consulta según su tipo y obligatoriedad. | Formularios de Pre-consulta | Web / Móvil | Media |
| RF-10 | Clasificación automática de casos (IA) | El sistema debe analizar las respuestas del formulario de pre-consulta mediante un modelo de IA para clasificar el nivel de urgencia y área temática del caso. | Clasificación y Asignación con IA | Web | Alta |
| RF-11 | Asignación sugerida de psicólogo | El sistema debe sugerir automáticamente el psicólogo más adecuado según especialidad, carga de trabajo y clasificación del caso, permitiendo confirmación manual del administrador. | Clasificación y Asignación con IA | Web | Alta |
| RF-12 | Chatbot de orientación inicial | El sistema debe ofrecer un chatbot conversacional que oriente al usuario nuevo sobre el proceso de registro, tipos de atención disponibles y primeros pasos. | Chatbot de Orientación | Web / Móvil | Media |
| RF-13 | Derivación desde el chatbot a soporte humano | El sistema debe permitir escalar la conversación del chatbot a un agente humano cuando la consulta supere su alcance. | Chatbot de Orientación | Web / Móvil | Media |
| RF-14 | Programación de citas | El sistema debe permitir agendar sesiones verificando la disponibilidad del psicólogo en tiempo real. | Agenda y Videoconferencia | Web / Móvil | Alta |
| RF-15 | Modificación y cancelación de citas | El sistema debe permitir reprogramar o cancelar citas respetando las políticas de anticipación configuradas por el centro. | Agenda y Videoconferencia | Web / Móvil | Alta |
| RF-16 | Teleconsulta por videollamada | El sistema debe habilitar sesiones de video en tiempo real entre paciente y psicólogo mediante conexión punto a punto (WebRTC). | Agenda y Videoconferencia | Web / Móvil | Alta |
| RF-17 | Chat de mensajería durante la sesión | El sistema debe permitir el intercambio de mensajes de texto entre paciente y psicólogo durante y fuera de la videoconsulta. | Agenda y Videoconferencia | Web / Móvil | Media |
| RF-18 | Recordatorios automáticos de citas | El sistema debe enviar notificaciones push/email antes de cada cita programada. | Agenda y Videoconferencia | Web / Móvil | Alta |
| RF-19 | Registro de estado de ánimo | El sistema debe permitir al paciente registrar diariamente su estado de ánimo mediante una interfaz simple tipo escala o emoji. | App Móvil del Paciente | Móvil | Alta |
| RF-20 | Ejercicios de mindfulness guiado | El sistema debe ofrecer contenido de mindfulness (audio/texto) accesible desde la app móvil del paciente. | App Móvil del Paciente | Móvil | Media |
| RF-21 | Gamificación de hábitos saludables | El sistema debe permitir el seguimiento de hábitos asignados mediante mecánicas de gamificación (rachas, puntos, logros). | App Móvil del Paciente | Móvil | Media |
| RF-22 | Historia clínica electrónica | El sistema debe centralizar el registro longitudinal del historial clínico del paciente, accesible únicamente por personal autorizado. | Historia Clínica y Seguimiento | Web | Alta |
| RF-23 | Registro de evolución por sesión | El sistema debe permitir al psicólogo documentar notas de evolución asociadas a cada sesión realizada. | Historia Clínica y Seguimiento | Web | Alta |
| RF-24 | Asignación de tareas terapéuticas | El sistema debe permitir al psicólogo asignar tareas o actividades entre sesiones, con fecha límite y objetivo definido. | Historia Clínica y Seguimiento | Web | Alta |
| RF-25 | Reporte de cumplimiento de tareas | El sistema debe permitir al paciente reportar el avance de sus tareas asignadas desde la app móvil. | Historia Clínica y Seguimiento | Móvil | Alta |
| RF-26 | Alertas de riesgo clínico | El sistema debe generar alertas automáticas al psicólogo cuando los datos de seguimiento (ánimo, respuestas de tests) indiquen un posible riesgo. | Alertas y Apoyo a la Decisión | Web | Alta |
| RF-27 | Panel de apoyo a la decisión clínica | El sistema debe presentar al psicólogo indicadores y tendencias del paciente que apoyen la toma de decisiones terapéuticas. | Alertas y Apoyo a la Decisión | Web | Media |
| RF-28 | Gestión de consentimientos y permisos | El sistema debe registrar y almacenar los consentimientos informados y autorizaciones del paciente para el tratamiento de sus datos. | Permisos y Documentación | Web / Móvil | Alta |
| RF-29 | Control de acceso a documentación clínica | El sistema debe restringir el acceso a documentos clínicos según el rol y la relación del usuario con el caso. | Permisos y Documentación | Web | Alta |
| RF-30 | Generación de reportes clínicos | El sistema debe permitir exportar historias clínicas y resúmenes de seguimiento en formato PDF. | Reportes | Web | Media |

## 3.8 Requisitos no funcionales

| ID | Categoría | Descripción | Prioridad |
|---|---|---|---|
| RNF-01 | Rendimiento | El sistema debe responder a las solicitudes de la API en un tiempo aceptable bajo condiciones normales de carga. | Alta |
| RNF-02 | Rendimiento | Las video consultas deben mantener calidad de audio/video estable en conexiones estándar. | Alta |
| RNF-03 | Escalabilidad | El sistema debe soportar el crecimiento en número de tenants y usuarios concurrentes sin degradar el servicio. | Alta |
| RNF-04 | Disponibilidad | La plataforma debe mantenerse operativa de forma continua, minimizando tiempos de inactividad. | Alta |
| RNF-05 | Seguridad – Autenticación | El sistema debe proteger las sesiones de usuario mediante mecanismos de autenticación robustos y tokens de vida limitada. | Alta |
| RNF-06 | Seguridad – Datos en tránsito | Toda comunicación entre cliente y servidor debe estar cifrada. | Alta |
| RNF-07 | Seguridad – Datos en reposo | La información clínica sensible almacenada debe estar protegida contra accesos no autorizados. | Alta |
| RNF-08 | Privacidad y cumplimiento normativo | El sistema debe manejar los datos de salud conforme a estándares de protección de datos aplicables. | Alta |
| RNF-09 | Aislamiento multi-tenant | La segregación de datos entre centros psicológicos debe garantizarse a nivel de infraestructura, no solo de aplicación. | Alta |
| RNF-10 | Control de acceso | El acceso a funcionalidades y datos debe restringirse estrictamente según el rol del usuario. | Alta |
| RNF-11 | Usabilidad | La interfaz debe ser comprensible e intuitiva para usuarios sin experiencia técnica previa, incluyendo pacientes en situación de vulnerabilidad emocional. | Media |
| RNF-12 | Accesibilidad | Las interfaces web y móvil deben ser utilizables por personas con discapacidad visual, motriz o cognitiva. | Media |
| RNF-13 | Compatibilidad | La plataforma debe funcionar correctamente en los principales navegadores y versiones recientes de sistemas móviles. | Media |
| RNF-14 | Mantenibilidad | El código debe seguir estándares que faciliten su mantenimiento y extensión por el equipo. | Media |
| RNF-15 | Portabilidad / Despliegue | El sistema debe poder desplegarse de forma reproducible en distintos entornos (desarrollo, staging, producción). | Alta |
| RNF-16 | Interoperabilidad | El sistema debe permitir la exportación de información clínica en formatos estándar para intercambio con otros sistemas. | Baja |
| RNF-17 | Auditabilidad | Toda acción crítica sobre datos clínicos debe quedar registrada de forma inmutable. | Alta |
| RNF-18 | Confiabilidad ante fallos | El sistema debe degradarse de forma controlada ante fallos de componentes externos (IA, videollamada, notificaciones). | Media |
| RNF-19 | Capacidad de la IA | Los modelos de clasificación y análisis de patrones deben ofrecer resultados consistentes y trazables. | Media |
| RNF-20 | Copias de seguridad | La información del sistema debe respaldarse periódicamente para prevenir pérdida de datos. | Alta |

## 3.9 Lista de casos de uso (web y móvil)

| ID | Descripción | Estado | Móvil | Web | Sprint |
|---|---|---|---|---|---|
| CU1 | Gestionar centros psicológicos y configuración Multi-Tenant | Propuesto | | X | SP0 |
| CU2 | Gestionar inicio de sesión y autenticación | Propuesto | X | X | SP0 |
| CU3 | Gestionar usuarios | Propuesto | | X | SP0 |
| CU4 | Gestionar roles y permisos | Propuesto | | X | SP0 |
| CU5 | Gestionar auditoría e historial de accesos | Propuesto | | X | SP4 |
| CU6 | Gestionar psicólogos y perfiles profesionales | Propuesto | | X | SP1 |
| CU7 | Gestionar pacientes | Propuesto | | X | SP1 |
| CU8 | Gestionar disponibilidad y carga de trabajo de psicólogos | Propuesto | | X | SP1 |
| CU9 | Consultar Dashboard e indicadores del centro psicológico | Propuesto | | X | SP1 |
| CU10 | Gestionar alertas de priorización y seguimiento | Propuesto | | X | SP1 |
| CU11 | Gestionar citas y agenda psicológica | Propuesto | X | X | SP1 |
| CU12 | Gestionar recordatorios y notificaciones automáticas | Propuesto | X | X | SP3 |
| CU13 | Gestionar teleconsultas y videoconferencias | Propuesto | X | X | SP1 |
| CU14 | Gestionar formulario previo a la consulta | Propuesto | X | X | SP2 |
| CU15 | Gestionar historia clínica psicológica | Propuesto | | X | SP2 |
| CU16 | Registrar y gestionar notas de sesión | Propuesto | | X | SP2 |
| CU17 | Gestionar evolución, tareas y seguimiento terapéutico | Propuesto | X | X | SP2 |
| CU18 | Gestionar consentimientos informados y autorizaciones | Propuesto | X | X | SP2 |
| CU19 | Gestionar cierre y derivación de casos psicológicos | Propuesto | | X | SP2 |
| CU20 | Interactuar con el chatbot de orientación al paciente | Propuesto | X | X | SP3 |
| CU21 | Clasificar motivo de consulta mediante Inteligencia Artificial | Propuesto | X | X | SP3 |
| CU22 | Sugerir asignación de paciente a psicólogo mediante Inteligencia Artificial | Propuesto | | X | SP3 |
| CU23 | Generar resúmenes clínicos asistidos por Inteligencia Artificial | Propuesto | | X | SP4 |
| CU24 | Detectar señales de riesgo y generar alertas mediante Inteligencia Artificial | Propuesto | | X | SP4 |
| CU25 | Generar y exportar reportes administrativos y clínicos | Propuesto | | X | SP4 |
| CU26 | Gestionar pagos y estado de cuenta del paciente | Propuesto | | X | SP4 |
| CU27 | Gestionar inicio de sesión y autenticación en la aplicación móvil | Propuesto | X | | SP3 |

## 3.10 Paquetes y casos de Uso

**Paquete 1 — Administración, Seguridad y Multi-Tenant:** CU1, CU2, CU3, CU4, CU5 y CU27.

- CU1. Gestionar centros psicológicos y configuración Multi-Tenant
- CU2. Gestionar inicio de sesión y autenticación
- CU3. Gestionar usuarios
- CU4. Gestionar roles y permisos
- CU5. Gestionar auditoría e historial de accesos
- CU27. Gestionar inicio de sesión y autenticación en la app móvil

**Paquete 2 — Gestión Clínica y de Profesionales:** CU6, CU7, CU8, CU15, CU16 y CU19.

- CU06. Gestionar psicólogos y perfiles profesionales
- CU07. Gestionar pacientes
- CU08. Gestionar disponibilidad y carga de trabajo de psicólogos
- CU15. Gestionar historia clínica psicológica
- CU16. Registrar y gestionar notas de sesión
- CU19. Gestionar cierre de casos psicológicos

**Paquete 3 — Agenda, Comunicación y Seguimiento:** CU9, CU10, CU11, CU12, CU13 y CU17.

- CU09. Consultar Dashboard e indicadores del centro psicológico
- CU10. Gestionar alertas de priorización y seguimiento
- CU11. Gestionar citas y agenda psicológica
- CU12. Gestionar recordatorios y notificaciones automáticas
- CU13. Gestionar teleconsultas y videoconferencias
- CU17. Gestionar evolución, tareas y seguimiento terapéutico

**Paquete 4 — Formularios, Consentimientos y Documentación:** CU14 y CU18.

- CU14. Gestionar formulario previo a la consulta
- CU18. Gestionar consentimientos informados y autorizaciones

**Paquete 5 — Inteligencia Artificial y Chatbot:** CU20, CU21, CU22, CU23 y CU24.

- CU20. Interactuar con el chatbot de orientación al paciente
- CU21. Clasificar motivo de consulta mediante IA
- CU22. Sugerir asignación de paciente a psicólogo mediante IA
- CU23. Generar resúmenes clínicos asistidos por IA
- CU24. Detectar señales de riesgo y generar alertas mediante IA

**Paquete 6 — Reportes y Pagos:** CU25 y CU26.

- CU25. Generar y exportar reportes administrativos y clínicos
- CU26. Gestionar pagos y estado de cuenta del paciente

## 3.11 Planificación Sprint (Diagrama de Gantt)

> Tabla con columnas de calendario (25-27 Ago., 08-10 Sep., 06-08 Oct., 03-05 Nov., 24-26 Nov.) que en el documento original se representan como celdas de un diagrama de Gantt (marcas visuales por periodo). A continuación se transcribe la identificación de cada tarea y el Sprint al que pertenece; las marcas de fecha específicas dentro del Gantt no contienen texto adicional más allá de la ubicación visual de la barra.

| ID | Descripción | Sprint |
|---|---|---|
| SP0-1 | Preparación y configuración inicial del proyecto | SP0 |
| SP0-2 | Inicio de sesión y autenticación | SP0 |
| SP0-3 | Gestión de usuarios, roles y permisos | SP0 |
| SP0-4 | Configuración de arquitectura Multi-Tenant | SP0 |
| SP1-1 | Gestión de psicólogos y perfiles profesionales | SP1 |
| SP1-2 | Gestión de pacientes | SP1 |
| SP1-3 | Gestión de disponibilidad y carga de trabajo | SP1 |
| SP1-4 | Dashboard e indicadores principales | SP1 |
| SP1-5 | Gestión de alertas de priorización | SP1 |
| SP1-6 | Gestión de citas y agenda psicológica | SP1 |
| SP1-7 | Gestión de videoconferencias y teleconsultas | SP1 |
| SP2-1 | Formulario previo a la consulta | SP2 |
| SP2-2 | Gestión de historia clínica psicológica | SP2 |
| SP2-3 | Registro y gestión de notas de sesión | SP2 |
| SP2-4 | Gestión de evolución y seguimiento terapéutico | SP2 |
| SP2-5 | Gestión de tareas y acuerdos terapéuticos | SP2 |
| SP2-6 | Gestión de consentimientos informados y autorizaciones | SP2 |
| SP2-7 | Gestión de cierre y derivación de casos | SP2 |
| SP3-1 | Registro e inicio de sesión en la aplicación móvil | SP3 |
| SP3-2 | Gestión de citas desde la aplicación móvil | SP3 |
| SP3-3 | Gestión de notificaciones y recordatorios | SP3 |
| SP3-4 | Seguimiento y tareas terapéuticas desde la aplicación móvil | SP3 |
| SP3-5 | Interacción con el chatbot de orientación | SP3 |
| SP3-6 | Clasificación del motivo de consulta mediante IA | SP3 |
| SP3-7 | Sugerencia de asignación de psicólogo mediante IA | SP3 |
| SP4-1 | Generación asistida de resúmenes clínicos | SP4 |
| SP4-2 | Detección de señales de riesgo y alertas prioritarias | SP4 |
| SP4-3 | Generación de reportes administrativos y clínicos | SP4 |
| SP4-4 | Exportación de reportes en PDF y Excel | SP4 |
| SP4-5 | Gestión de pagos y estado de cuenta | SP4 |
| SP4-6 | Auditoría, seguridad e historial de accesos | SP4 |
| SP4-7 | Pruebas finales e integración de la plataforma | SP4 |

---

# BIBLIOGRAFÍA

*(Transcrito tal como figura en el documento original, incluyendo el título "BIBLIÓGRAFA")*

## a. Libros y Literatura

- American Psychological Association. (2017). *Ethical principles of psychologists and code of conduct*. APA.
- Beck, J. S. (2011). *Cognitive behavior therapy: Basics and beyond* (2.ª ed.). Guilford Press.
- Colegio de Psicólogos de Bolivia. (2002). *Código de ética del psicólogo boliviano*. La Paz, Bolivia.
- Fernández-Ballesteros, R. (2013). *Evaluación psicológica: Conceptos, métodos y estudio de casos* (2.ª ed.). Ediciones Pirámide.
- Graham, S., Depp, C., Lee, E. E., Nebeker, C., Tu, X., Kim, H. C., & Jeste, D. V. (2019). Artificial intelligence for mental health and mental illnesses: An overview. *Current Psychiatry Reports*, 21(11), 1-15. https://doi.org/10.1007/s11920-019-1094-0
- Laudon, K. C., & Laudon, J. P. (2020). *Management information systems: Managing the digital firm* (16.ª ed.). Pearson.
- Organización Mundial de la Salud. (2022). *Informe mundial sobre salud mental: Transformar la salud mental para todos*. OMS. https://www.who.int/es/publications/i/item/9789240050860
- Pressman, R. S., & Maxim, B. R. (2020). *Ingeniería del software: Un enfoque práctico* (9.ª ed.). McGraw-Hill.
- Sommerville, I. (2016). *Software engineering* (10.ª ed.). Pearson.

## b. Sitios Web Especializados

- Angular Team. (2024). *Angular documentation*. Google. https://angular.dev/
- Django Software Foundation. (2024). *Django documentation*. https://www.djangoproject.com/
- Flutter Team. (2024). *Flutter documentation*. Google. https://flutter.dev/
- iClinic. (2024). *Software de gestión clínica y prontuario electrónico*. https://iclinic.com.br/
- MentalGest. (2024). *Software clínico para psicólogos y consultorios*. https://mentalgest.com/
- MentalGest. (2024). *Transparencia e inteligencia artificial en MentalGest*. https://mentalgest.com/transparencia-ia
- Organización Mundial de la Salud. (2022). *Salud mental: Fortalecimiento de nuestra respuesta*. OMS. https://www.who.int/es/news-room/fact-sheets/detail/mental-health-strengthening-our-response
- PostgreSQL Global Development Group. (2024). *PostgreSQL: The world's most advanced open source relational database*. https://www.postgresql.org/
- Psicología.io. (2024). *Plataforma de gestión para psicólogos y profesionales de la salud mental*. https://psicologia.io/
- SimplePractice. (2024). *Practice management software for EHR & telehealth*. https://www.simplepractice.com/
- Spring Health. (2024). *Precision mental healthcare platform*. https://www.springhealth.com/
- Spring Health. (2024). *Our approach to mental healthcare*. https://www.springhealth.com/our-approach
- Spring Health. (2024). *SpringCare: Comprehensive mental health support*. https://www.springhealth.com/what-we-do/springcare
- Talkspace. (2024). *Online therapy and psychiatry services platform*. https://www.talkspace.com/
- TherapyNotes. (2024). *Practice management software for mental health professionals*. https://www.therapynotes.com/

---

# ANEXOS

> Los anexos del documento original contienen capturas de pantalla de la plataforma real **MentalGest** (usada como referencia visual/funcional). A continuación se transcribe la descripción textual de cada anexo tal como figura en el documento (el contenido gráfico corresponde a capturas de pantalla de la interfaz de MentalGest).

## 1. Anexo A

**Recuperado de:** https://app.mentalgest.com/auth/register

**Descripción:** Formulario de Registro para el profesional de la salud mental de la plataforma MentalGest. La captura muestra una pantalla dividida en dos columnas: a la izquierda, el mensaje "Recupera tu tiempo libre. Gestiona tus consultas con IA", con bullets de características (agenda inteligente y resúmenes con IA, sincronización con Google Calendar y Google Drive, historial clínico estructurado y gestión de pacientes en un solo lugar, privacidad garantizada); a la derecha, un formulario de registro "Comienza tu prueba gratuita" con selección de tipo de usuario (Profesional de salud mental / Clínica / Paciente), opción de continuar con Google, y campos de Nombre y Apellidos, Email, Teléfono, Contraseña y Confirmar contraseña.

## 2. Anexo B

**Recuperado de:** https://app.mentalgest.com/professional

**Descripción:** Dashboard de la plataforma MentalGest. Muestra un panel principal con menú lateral (Dashboard, Pacientes, Citas, Calendario, Reservas, Pagos, Paquetes, Consentimientos, Formularios, Biblioteca, Disponibilidad, Reportes), saludo al profesional, indicadores de Pacientes Activos, Sesiones Completadas, Tasa de Conversión y Tasa de Asistencia, además de un listado de próximas citas y métricas adicionales de sesiones completadas hoy y total de sesiones.

## 3. Anexo C

**Recuperado de:** https://app.mentalgest.com/professional/patients

**Descripción:** Apartado de Gestión de Pacientes de la plataforma MentalGest. Muestra el listado de pacientes con opciones de búsqueda por nombre o email, filtros (Todos / Activos / Inactivos), botones de "Importar pacientes" y "+ Nuevo paciente", y una ficha resumida de paciente con nombre, email, teléfono, próxima cita y sesiones completadas, con acciones de "Ver perfil" y "Ver citas".

## 4. Anexo D

**Recuperado de:** https://app.mentalgest.com/professional/patients/new

**Descripción:** Apartado de Registro de nuevos pacientes de la plataforma MentalGest. Formulario "Nuevo paciente" con selección de Tipo de paciente (Adulto / Niño-a), tipo de ficha (Ficha rápida / Ficha completa), sección de Identificación con campos de Nombre completo, Email (opcional), Documento de identidad y Teléfono, checkbox para "Recibir recordatorios de citas" (con nota de que si está desactivado el paciente no recibirá recordatorios por WhatsApp), y botones "Cancelar" / "Crear paciente".

## 5. Anexo E

**Recuperado de:** https://app.mentalgest.com/professional/leads

**Descripción:** Gestión de Reservas de la plataforma MentalGest. Muestra el apartado "Reservas" con pestañas de estado (Pendientes, Aprobados, Cancelados), filtro por origen, y un listado de solicitudes de reserva con nombre del paciente, origen (Reserva de cita, Nuevo contacto, Cita 1:1 horas, Reserva manual), datos de contacto, fecha/hora y modalidad (Presencial / Videollamada), con acciones "Aprobar" o "Rechazar".

## 6. Anexo F

**Recuperado de:** https://app.mentalgest.com/professional/reports

**Descripción:** Apartado de Reportes de la plataforma MentalGest. Muestra pestañas de "Citas" y "Paquetes", indicadores de Total de Ingresos, Citas Totales, Tasa de Asistencia y Nuevos Pacientes, un gráfico de "Evolución de ingresos y citas", un gráfico de dona de "Fuentes de reserva" (creado por consultorio / reserva manual) y una tabla de "Retención de pacientes (continuidad terapéutica)" por etapa de sesión (primera, segunda, cuarta, octava sesión) con cantidad de pacientes y porcentaje de retención.

## 7. Anexo G

**Recuperado de:** https://app.mentalgest.com/professional/availability

**Descripción:** Apartado de Gestión de Disponibilidad del profesional para dar atención al cliente, en la plataforma MentalGest. Muestra la pantalla "Horarios de disponibilidad" donde se configuran los horarios de atención por día de la semana (por ejemplo, Lunes con dos turnos: 9:00am-6:00pm Presencial y virtual, y 9:00pm-10:00pm Virtual; Martes marcado como "No disponible"), con opción de "Agregar turno" y botones "Descartar cambios" / "Guardar cambios".

---

*Fin de la transcripción íntegra del documento "GRUPO_9_Sistema_Psicologico" (86 páginas). Este archivo Markdown reproduce el contenido textual completo del perfil de proyecto: introducción, antecedentes, casos de estudio, justificación, descripción y formulación del problema, objetivos, alcance (9 módulos), elementos del SIBC, tecnología, costos, beneficios, marco teórico, marco de trabajo SCRUM, herramientas tecnológicas, y el capítulo de requerimientos completo (equipo SCRUM, definiciones, funciones del producto, Product Backlog de 73 ítems, 30 requisitos funcionales, 20 requisitos no funcionales, 27 casos de uso agrupados en 6 paquetes, planificación de sprints), bibliografía y anexos.*
