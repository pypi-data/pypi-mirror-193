"""
这里存放一些可能需要修改的参数
"""
default_headers = {
            'Referer':
            'https://kns.cnki.net/kns8/defaultresult/index',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        }

para_dic = {
    'SCDB': '总库',
    'CJFQ': '学术期刊',
    'CDMD': '学位论文',
    'CDFD': '博士',
    'CMFD': '硕士',
    'CIPD': '会议',
    'CPFD': '国内会议',
    'IPFD': '国际会议',
    'CPVD': '会议视频',
    'CCND': '报纸',
    'CYFD': '年鉴',
    'BDZK': '图书',
    'WBFD': '中文图书',
    'WWBD': '外文图书',
    'SCOD': '专利',
    'SCPD': '中国专利',
    'SOPD': '海外专利',
    'CISD': '标准',
    'SCSF': '国家标准',
    'SCHF': '行业标准',
    'SMSD': '标准题录',
    'SNAD': '成果',
    'CCJD': '学术辑刊',
    'GXDB_SECTION': '古籍',
    'CJFN': '特色期刊',
    'CCVD': '视频'
}

search_mode_list = {
            "SU":("主题","SU","%=",""),
            "TKA":("篇关摘","TKA","%=",""),
            "KY":("关键词","KY","=",""),
            "TI":("主题","SU","%=",""),
            "FT":("全文","FT","%=",""),
            "FU":("基金","FU","%",""),
            "AB":("摘要","AB","%=",""),
            "CO":("小标题","CO","%=",""),
            "RF":("参考文献","RF","%=",""),
            "CLC":("分类号","CLC","=","??"),
            "LY":("文献来源","LY","%=",""),
            "DOI":("DOI","DOI","=","?"),
            "AU":("作者","AU","=",""),
            "FI":("第一作者","FI","=",""),
            "RP":("通讯作者","RP","","")
        }