touch coordinate
for l in `find ./kml | grep "kml.*kml"`
do
python kml_to_coordinates.py ${l} >> coordinate
done
cat coordinate | python coordinates_to_image.py
rm coordinate
