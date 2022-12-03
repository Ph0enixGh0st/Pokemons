import folium
import json
from datetime import datetime as dt

from django.utils import timezone
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    localtime=dt.now()
    pokemons = PokemonEntity.objects.filter(appeared_at__lt=localtime, disappeared_at__gt=localtime).select_related('pokemon')

    pokemons_on_page = []
    pokemon_types = Pokemon.objects.all().select_related('previous_evolution')
    for pokemon in pokemon_types:
        if pokemon.image:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': request.build_absolute_uri(pokemon.image.url),
                'title_ru': pokemon.title,
            })
        else:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': DEFAULT_IMAGE_URL,
                'title_ru': pokemon.title,
            })

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        pokemon_found = get_object_or_404(Pokemon, id=pokemon.pokemon_id)
        add_pokemon(
        folium_map, pokemon.lat,
        pokemon.lon,
        request.build_absolute_uri(pokemon_found.image.url)
        )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    pokemons_one_page = {}
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    pokemons_one_page={
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'title_ru': pokemon.title,
        'title_jp': pokemon.title_jp,
        'title_en': pokemon.title_en,
        'description': pokemon.description,
        }

    next_evo = pokemon.next_evolutions.first()
    if next_evo:
        pokemons_one_page['next_evolution']={
            'title_ru': pokemon.next_evolutions.first().title,
            'pokemon_id': pokemon.next_evolutions.first().id,
            'img_url': request.build_absolute_uri(pokemon.next_evolutions.first().image.url)
            }

    prev_evo = pokemon.previous_evolution
    if prev_evo:
        pokemons_one_page['previous_evolution']={
            'title_ru': pokemon.previous_evolution.title,
                'pokemon_id': pokemon.previous_evolution.id,
                'img_url': request.build_absolute_uri(pokemon.previous_evolution.image.url)
            }

    if pokemon.image:
        pokemons_one_page['img_url'] = request.build_absolute_uri(pokemon.image.url)
    else:
        pokemons_one_page['img_url'] = DEFAULT_IMAGE_URL

    localtime=dt.now()
    pokemons = pokemon.entities.filter(appeared_at__lt=localtime, disappeared_at__gt=localtime).select_related('pokemon')
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        pokemon_found = get_object_or_404(Pokemon, id=pokemon.pokemon_id)
        add_pokemon(
        folium_map, pokemon.lat,
        pokemon.lon,
        request.build_absolute_uri(pokemon_found.image.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemons_one_page
    })