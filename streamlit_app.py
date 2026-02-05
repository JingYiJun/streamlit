# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2026)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Streamlit AudioColumn 示例应用.

演示如何在 dataframe 中使用 st.column_config.AudioColumn 来播放音频。
"""

import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="AudioColumn Demo",
    page_icon="🎵",
    layout="centered",
)

st.title("🎵 AudioColumn 示例")

st.markdown("""
这个示例演示如何使用 `st.column_config.AudioColumn` 在 dataframe 中嵌入可播放的音频。
""")

# 创建包含音频 URL 的数据
audio_url = (
    "https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3"
)

df = pd.DataFrame(
    {
        "track_name": ["Sample Track 1", "Sample Track 2", "Sample Track 3"],
        "artist": ["Artist A", "Artist B", "Artist C"],
        "audio": [audio_url, audio_url, audio_url],
        "duration": ["0:30", "0:30", "0:30"],
    }
)

st.subheader("音频播放器表格")

st.dataframe(
    df,
    column_config={
        "track_name": st.column_config.TextColumn(
            label="曲目名称",
            width="medium",
        ),
        "artist": st.column_config.TextColumn(
            label="艺术家",
            width="small",
        ),
        "audio": st.column_config.AudioColumn(
            label="播放",
            width="medium",
            help="点击播放音频预览",
        ),
        "duration": st.column_config.TextColumn(
            label="时长",
            width="small",
        ),
    },
    hide_index=True,
    use_container_width=True,
)

st.markdown("---")

st.subheader("代码示例")

st.code(
    """
import pandas as pd
import streamlit as st

audio_url = "https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3"

df = pd.DataFrame({
    "track_name": ["Sample Track"],
    "audio": [audio_url],
})

st.dataframe(
    df,
    column_config={
        "audio": st.column_config.AudioColumn(
            label="播放",
            width="medium",
            help="点击播放音频预览",
        ),
    },
)
""",
    language="python",
)
