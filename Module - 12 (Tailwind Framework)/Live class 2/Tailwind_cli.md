# Installation
- Obossoye node.js install thakte hbe then,
- jei project e achi oi project e nicher command dite hbe
- `npm install tailwindcss @tailwindcss/cli`
>Proti project er jonne alada alada vabe evabe install korte hobe

## Process
- input and output er .css type file khulbo
- tailwind er jnne ja ja lagbe ta input e likhbo
- output e auto generate hoye jabe tailwind
- @import "tailwindcss"; - input.css e paste krbo then,
- terminal e input r output er path declare krbo : `npx @tailwindcss/cli -i ./input.css -o ./output.css --minify` - ei command diye then,
- output.css link krbo
> extra jde css likhte chai shb input.css e likhbo 
>and ja ja likhbo tar shb output.css er <b>@layer utilities</b> e add hobe

## States
- Hover tailwind diye handle kora onk easy
```sh
hover:bg-red-900 
hover:text-white
```
- core concepts in tailwind css are most important

>Link: `https://tailwindcss.com/docs/hover-focus-and-other-states`

## Responsiveness
- Tailwind css mobile first design
```sh
sm:grid-cols-3
md:grid-cols-1
```
>Link: `https://tailwindcss.com/docs/responsive-design`

## Custom Component Style
- Jode emon hoy, akta property er jonne same style onkbar use korte hocce tahole,
- first e component nam er layer baniye tar moddhe likhbo jemon,
```sh
@layer components{
    .btn{
        @apply px-4 py-2 bg-red-400 rounded-2xl;
    }
}
```
- same style bar bar na likhe akta variable er moto baniye sheita use kora
> eita korar best practice hocce button and kicu link style er somoy use kora. tasara eita use hoy na

## Custom The Tailwind
- theme er moddhe jekono properties niye amra amader iccha moto tailwind customize krte pari
```sh
@theme{
    --color-any_name_of_the_style_I_want_to_give: #abc25a- this is style;
}
```
>More Deitails: `https://tailwindcss.com/docs/theme`
## Best Practice
> Component design er somoy <b>@layer component</b> name e layer baiye kaj kora
<br>

> <b>@layer utilities</b> use korbo jkhn nijer moto custom css add korabo
<br>

> overall kono design dite chaile jemon center e ana, font-style dewa er jonno  <b>@layer base</b> use korbo

## Choosing any design from Website
> Link: `https://flowbite.com/docs/components/card/`
<br>

> Link: `https://daisyui.com/docs/intro/`