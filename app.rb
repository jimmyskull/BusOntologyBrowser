require 'sparql/client'

file = "http://localhost:8890/sparql"

#uri = RDF::URI.new(file)
#puts(uri)
#puts RDF::Graph.load(uri, :format => :rdfxml)

sparql = SPARQL::Client.new(file)

query = sparql.select.where([:s, :p, :o]).offset(100).limit(10)

query.each_solution do |solution|
  puts solution[:s]
end
