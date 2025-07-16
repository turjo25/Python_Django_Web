# Flexbox
- onkgulo item thakle sheigulo ke shajanor jonne
- akta single row or column e data kiave shajano thakbe ta define kore
## display: flex;
- shbgulo content same line e anar jonne
## flex-wrap: wrap;
- container er bayre na jaye automatically porer row te element fit korabe
## flex-grow:1;
- particular item er jnne emon condition dile shey faka space baki shbtuku niye boshe jabe
## flex-shrink:2;
- jkhn space soto hobe onno item er shapekkhe ei item er size double soto hbe


# Grid
- jode tabuler format e data shajano lage, means: excel sheet er moto multiple row column niye kaj kora lage tahole grid use korbo
## display:grid;
- declaration of grid property
## grid-template-rows: 100px 100px 100px;
- how many rows there will be in grid - in this case its 3
## grid-template-columns: 100px 100px 100px;
- how many columns there will be in grid - in this case its 3
## grid-auto-rows: 200px;
- extra rows ashle ei jayga allocate hbe
## grid-auto-columns: 200px;
- extra rows ashle ei jayga allocate hbe
## grid-auto-flow: column;
- column age puron kore shajabe
## grid-auto-flow: row;
- row age puron kore shajabe
## 1fr unit 
- puro grid er width niye nibe. grid multiple thakle width shoman vage vag hoye trpor allocate hbe
## grid-row: 2 / 4;
## grid-column: 1 / 5;
- kono item row or column borabor kotokhani jayga nibe
- 2/4 means: 2 to 4 no. row porjonto jayga occupy krbe 
- 1/5 means: 1 to 5 no. column porjonto jayga occupy krbe

## Media Queries
- Fully responsive website bananor jonne
- @media (max-width: 700px) - maximum width 700px porjonto kaj korbe
