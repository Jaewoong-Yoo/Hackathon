path = ""
figs = []
def append_html(file = None,fig = None,mode = 'a'):
    '''여러 개의 plotly figure 를 저장해주는 함수
       file: 확장자 뺀 파일이름
       fig: figure or figure list
       mode: a: append, w:write'''
    with open(path+f'{file}.html', mode= mode) as f:
        f.write( fig.to_html(full_html=False,
                         include_plotlyjs='cdn'))

"""
fig = go.Figure()
여기에 fig 들 계속 재생산해서 밑에서 append 하시면 됩니다!
"""
figs.append(fig))
for fig in figs:
    append_html(file='plotly_result',fig=fig)