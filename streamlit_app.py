import random
import streamlit as st

st.set_page_config(
    page_title='점심 메뉴 추천기',
    page_icon=':fork_and_knife:',
    layout='centered',
)

st.title('오늘 점심은 뭘 먹을까?')
st.write('버튼을 누르면 오늘 점심에 무엇을 먹을지 랜덤으로 추천해 드립니다.')

menu_categories = {
    '한식': [
        '김치찌개', '된장찌개', '순두부찌개', '부대찌개', '갈비찜', '제육볶음',
        '불고기', '닭갈비', '비빔밥', '볶음밥', '오므라이스', '돈까스',
        '김밥', '도시락', '떡국', '설렁탕', '삼계탕', '감자탕',
    ],
    '중식': [
        '짜장면', '짬뽕', '볶음밥', '탕수육', '마파두부', '양장피', '마라탕',
        '마라샹궈', '유산슬', '깐풍기',
    ],
    '일식/아시아': [
        '초밥', '회덮밥', '연어덮밥', '우동', '냉우동', '카레라이스',
        '라멘', '돈부리', '덮밥', '테판야끼', '토스트',
    ],
    '양식': [
        '피자', '파스타', '리조또', '스테이크', '햄버거', '샌드위치',
        '샐러드', '그릴치킨', '감바스', '에그베네딕트',
    ],
    '분식/간편식': [
        '떡볶이', '쫄면', '순대', '김말이', '튀김', '핫도그', '토스트',
        '컵밥', '참치김밥', '샌드위치',
    ],
    '국/탕': [
        '순댓국', '곰탕', '설렁탕', '삼계탕', '감자탕', '우거지국',
        '갈비탕', '해장국', '북엇국',
    ],
}

selected_categories = st.multiselect(
    '보고 싶은 카테고리를 선택하세요',
    list(menu_categories.keys()),
    default=list(menu_categories.keys()),
)

st.subheader('선택된 카테고리 메뉴 목록')
if selected_categories:
    for category in selected_categories:
        with st.expander(category, expanded=False):
            st.write(', '.join(menu_categories[category]))
else:
    st.warning('최소 하나의 카테고리를 선택해 주세요.')

st.subheader('원하는 메뉴를 직접 추가해 보세요')
custom_text = st.text_area(
    '추가하고 싶은 메뉴가 있다면 쉼표(,)로 구분하여 입력하세요.',
    value='',
    height=120,
)

menu_candidates = []
for category in selected_categories:
    menu_candidates.extend(menu_categories[category])

custom_menus = [item.strip() for item in custom_text.split(',') if item.strip()]
menu_candidates.extend(custom_menus)
menu_candidates = list(dict.fromkeys(menu_candidates))

if not menu_candidates:
    st.warning('추천할 메뉴를 최소 하나 이상 선택하거나 추가해 주세요.')
else:
    if st.button('랜덤 점심메뉴 추천'):
        recommendation = random.choice(menu_candidates)
        st.success(f'오늘 점심 추천: **{recommendation}**')
        st.balloons()
    else:
        st.info('버튼을 눌러 점심 메뉴를 추천받아 보세요!')
