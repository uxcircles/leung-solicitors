/* Leung & Co Law map: MapLibre + OpenFreeMap vector tiles in the seal palette. Pin = the firm's phoenix seal. */
(() => {
  const C = {
    land: '#f4eee4', building: '#e7dccb', buildingLine: '#d9cab4', park: '#e2e8d2', water: '#cfdbe0',
    road: '#ffffff', roadCase: '#e0d3c0', major: '#fff7ef', majorCase: '#e8b597',
    rail: '#bfae9b', label: '#201a17', labelSoft: '#6f645b', halo: '#f4eee4',
  };
  const name = ['coalesce', ['get', 'name:en'], ['get', 'name_en'], ['get', 'name']];
  const width = (a, b, c) => ['interpolate', ['exponential', 1.6], ['zoom'], 13, a, 16, b, 18, c];
  const major = ['match', ['get', 'class'], ['motorway', 'trunk', 'primary', 'secondary'], true, false];
  const minor = ['match', ['get', 'class'], ['tertiary', 'minor', 'service', 'street', 'residential'], true, false];
  const style = {
    version: 8,
    glyphs: 'https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf',
    sources: { omt: { type: 'vector', url: 'https://tiles.openfreemap.org/planet' } },
    layers: [
      { id: 'land', type: 'background', paint: { 'background-color': C.land } },
      { id: 'park', type: 'fill', source: 'omt', 'source-layer': 'park', paint: { 'fill-color': C.park } },
      { id: 'green', type: 'fill', source: 'omt', 'source-layer': 'landuse', filter: ['match', ['get', 'class'], ['park', 'grass', 'cemetery', 'pitch', 'playground'], true, false], paint: { 'fill-color': C.park } },
      { id: 'water', type: 'fill', source: 'omt', 'source-layer': 'water', paint: { 'fill-color': C.water } },
      { id: 'building', type: 'fill', source: 'omt', 'source-layer': 'building', minzoom: 13, paint: { 'fill-color': C.building, 'fill-outline-color': C.buildingLine } },
      { id: 'rail', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: ['match', ['get', 'class'], ['rail', 'transit'], true, false], paint: { 'line-color': C.rail, 'line-width': 1.4, 'line-dasharray': [3, 2] } },
      { id: 'road-case', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: minor, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.roadCase, 'line-width': width(1.5, 6, 20) } },
      { id: 'major-case', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: major, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.majorCase, 'line-width': width(3, 10, 30) } },
      { id: 'road', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: minor, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.road, 'line-width': width(1, 4.5, 17) } },
      { id: 'major', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: major, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.major, 'line-width': width(2, 8, 27) } },
      { id: 'road-label', type: 'symbol', source: 'omt', 'source-layer': 'transportation_name', minzoom: 14, layout: { 'symbol-placement': 'line', 'text-field': name, 'text-font': ['Noto Sans Regular'], 'text-size': 11 }, paint: { 'text-color': C.labelSoft, 'text-halo-color': C.halo, 'text-halo-width': 1.4 } },
      { id: 'area-label', type: 'symbol', source: 'omt', 'source-layer': 'place', filter: ['match', ['get', 'class'], ['suburb', 'quarter', 'neighbourhood'], true, false], layout: { 'text-field': ['upcase', name], 'text-font': ['Noto Sans Bold'], 'text-size': 11, 'text-letter-spacing': 0.18, 'text-max-width': 8 }, paint: { 'text-color': C.labelSoft, 'text-halo-color': C.halo, 'text-halo-width': 1.4 } },
    ],
  };
  window.lcMap = (box) => {
    const data = JSON.parse(document.getElementById('map-data').textContent);
    const { maplibregl } = window;
    const holder = document.createElement('div');
    holder.className = 'mapbox';
    box.insertBefore(holder, box.querySelector('.map-open'));
    const phone = window.matchMedia('(max-width: 760px)').matches;
    const map = new maplibregl.Map({
      container: holder, style, center: data.home, zoom: phone ? 14 : 14.6, maxZoom: 18, minZoom: 11,
      dragRotate: false, pitchWithRotate: false, cooperativeGestures: true, attributionControl: { compact: true },
    });
    map.touchZoomRotate.disableRotation();
    if (!phone) map.addControl(new maplibregl.NavigationControl({ showCompass: false }), 'top-left');
    const pin = document.createElement('div');
    pin.className = 'map-pin';
    pin.innerHTML = `<span class="pin"><img src="${data.mark}" alt=""></span><span class="pin-label">${data.label}</span>`;
    new maplibregl.Marker({ element: pin, anchor: 'top', offset: [0, -30] }).setLngLat(data.home).addTo(map);
    return map;
  };
})();
