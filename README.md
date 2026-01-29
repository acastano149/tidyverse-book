# Tidyverse para Pandas Users: Edición Sports Science

Libro interactivo de Quarto para aprender **R/Tidyverse** orientado a **Sport Scientists** que ya conocen **Python/Pandas**.

## 📖 Descripción

Este libro replica la estructura del `pandas-sports-book-main` pero invirtiendo la dirección: enseña R/Tidyverse a usuarios que ya dominan Python/Pandas.

## 🚀 Cómo usar

### Renderizar el libro

```bash
cd tidyverse-sports-book-main
quarto render
```

El libro se generará en la carpeta `_book/`.

### Visualizar en desarrollo

```bash
quarto preview
```

## 📚 Contenido

### Parte 1: Fundamentos
1. **Introducción**: De DataFrames a Tibbles
2. **Flujo de Trabajo**: El Pipe `%>%`

### Parte 2: Manipulación de Datos
3. **Verbos I**: select, filter, arrange
4. **Verbos II**: mutate, rename, case_when
5. **Agregación**: group_by + summarise

### Parte 3: Transformación y Combinación
6. **Reshaping**: pivot_longer, pivot_wider
7. **Joins**: left_join, inner_join, anti_join

### Parte 4: Visualización y Producción
8. **ggplot2**: Gramática de gráficos
9. **Missing Data**: Manejo de NA
10. **Rendimiento**: Optimización

### Parte 5: Análisis Avanzado en Fútbol
11. **Visualización Avanzada**: Campos, shotmaps, heatmaps
12. **Estadísticas**: Correlación, regresión, xG
13. **APIs**: StatsBombR, worldfootballR
14. **Machine Learning**: tidymodels
15. **Shiny**: Web Apps interactivas
16. **Scouting**: Radar charts
17. **Expected Threat**: xT
18. **Passing Networks**: Redes de pases
19. **Pitch Control**: Control del campo
20. **Simulación**: Monte Carlo para partidos

## ⚙️ Requisitos

- Quarto >= 1.4
- R >= 4.1
- Paquetes: tidyverse, ggplot2, shiny

## 📝 Licencia

Uso educativo.
