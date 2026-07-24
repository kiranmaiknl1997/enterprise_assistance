from ingestion.loader import DocumentLoader

docs = DocumentLoader('documents').load_documents()

bread = [d for d in docs if d.metadata.get('source') == 'Bread Client KT.pptx']
print('BREAD_SLIDES', len(bread))
for d in bread:
    print('--- SLIDE', d.metadata.get('slide'), 'TITLE:', d.metadata.get('slide_title'))
    print(d.page_content)
    print('---')

client = [d for d in docs if d.metadata.get('source') == 'client presentation doc.docx']
print('CLIENT_SECTIONS', len(client))
for i, d in enumerate(client[:10], 1):
    print('=== SECTION', i, '===')
    print(d.page_content)
    print('---')

mart = [d for d in docs if d.metadata.get('source') == 'Marketing Mart.pdf']
print('MARKETING_MART', len(mart))
for i, d in enumerate(mart[:5], 1):
    print('=== PAGE', i, '===')
    print(d.page_content[:2000])
    print('---')

snapshot = [d for d in docs if d.metadata.get('source') == 'MAPPING-DOCUMENT.xlsx' and 'snapshot_id' in (d.page_content or '').lower()]
print('SNAPSHOT_ROWS', len(snapshot))
for i, d in enumerate(snapshot[:5], 1):
    print('=== ROW', i, '===')
    print(d.page_content)
    print('---')

kube = [d for d in docs if 'kubernetes' in (d.page_content or '').lower()]
print('KUBERNETES', len(kube))
for i, d in enumerate(kube[:5], 1):
    print('=== KUBE SOURCE', d.metadata.get('source'), '===')
    print(d.page_content)
    print('---')
