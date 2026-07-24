from pathlib import Path
from dotenv import load_dotenv
from agents.retriever import RetrieverAgent

load_dotenv()
project_root = Path(__file__).resolve().parent
persist_dir = project_root / 'database' / 'chroma_db'
print('persist_dir exists', persist_dir.exists())
print('files:', sorted(str(f.relative_to(persist_dir)) for f in persist_dir.rglob('*') if f.is_file()))

retriever = RetrieverAgent()
vector = retriever.vector_store

print('vector store type', type(vector))

try:
    one = vector.get(limit=1)
    print('get limit 1 result keys', list(one.keys()))
    print('ids count', len(one.get('ids', [])))
    print('metadatas count', len(one.get('metadatas', [])))
    if one.get('metadatas'):
        print('first metadata sample', one['metadatas'][0])
    if one.get('documents'):
        print('first document sample', repr(one['documents'][0])[:300])
except Exception as e:
    print('GET ERROR:', type(e).__name__, e)

try:
    results = vector.get(where={'table': 'bill_promo_fct', 'target_column': 'snapshot_id'}, include=['metadatas', 'documents', 'ids'])
    print('filter result keys', list(results.keys()))
    print('filter ids count', len(results.get('ids', [])))
    if results.get('ids'):
        print('sample metadata', results['metadatas'][0])
        print('sample doc', repr(results['documents'][0])[:500])
except Exception as e:
    print('FILTER ERROR:', type(e).__name__, e)

try:
    sim = vector.similarity_search('Transformation for SNAPSHOT_ID in BILL_PROMO_FCT', k=5)
    print('similarity_search count', len(sim))
    if sim:
        print('sample sim metadata', getattr(sim[0], 'metadata', None))
        print('sample sim text', repr(getattr(sim[0], 'page_content', ''))[:300])
except Exception as e:
    print('SIM ERROR:', type(e).__name__, e)
