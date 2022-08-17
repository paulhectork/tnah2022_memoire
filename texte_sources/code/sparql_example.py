from SPARQLWrapper import SPARQLWrapper, SPARQLExceptions, JSON, XML
import json
import sys
import re
import os

# --------------------------------------------------
# launch a simple sparql query (all paintings by
# natalia gontcharova) and save the output to
# ../appendix in order to have examples of the
# sparql return formats
# --------------------------------------------------

appendix = os.path.abspath(
	os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
   	"../annexes"
	)
)  # output dir

def sparql(format:str):
	"""
	launch the sparql query
	:param format: the sparql response format
	:return: None
	"""
	if not re.search("^(json|xml)$", format):
		print(f"invalid sparql return format: {format}")
		sys.exit(1)

	out = None
	endpoint = SPARQLWrapper(
		"https://query.wikidata.org/sparql",
		agent="katabot/1.0 (https://katabase.huma-num.fr/) python/SPARQLwrapper/2.0.0"
	)
	query = """
		SELECT ?painting ?paintingLabel
		WHERE {
	  		?painting wdt:P170 wd:Q232391 .
			SERVICE wikibase:label {
	    		bd:serviceParam wikibase:language "en" .
			}
		}
		LIMIT 5
	"""
	endpoint.setQuery(query)

	if format == "json":
		endpoint.setReturnFormat(JSON)
	else:
		endpoint.setReturnFormat(XML)
	results = endpoint.queryAndConvert()

	# save results
	with open(f"{appendix}/sparql_result.{format}", mode="w") as fh:
		if format == "json":
			# save a pretty json
			json.dump(results, fh, indent=4)
		else:
			fh.write(results.toprettyxml())

	return None

if __name__ == "__main__":
	sparql("json")
	sparql("xml")
