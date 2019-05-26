# Ｗine tasting

* ##### Data set:[Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)

# 1. Introduction

​	[Somm](https://www.imdb.com/title/tt2204371/)是一部描述四個品酒師考取Master Sommelier的電影，在當中有項測試是盲品，再不看酒標的狀態下，憑藉著酒的氣味、顏色、香味去判斷葡萄酒的品種、產區、品牌、年份，甚至哪片葡萄園。

​	在此，我們想要根據品酒師喝下葡萄酒後說出來的話來猜測這瓶酒的葡萄品種，讓我們的機器也能擁有盲品的能力。

# 2. Data 

## 2.1 Description

- #### Flie Content

 | Data                 | Size     | p(variables) | n(observations) |
| -------------------- | -------- | ------------ | --------------- |
| winemag-data-130k-v2 | 50.46 MB | 119988       | 13              |

- #### Part of the data (winemag-data-130k-v2)

 因資料過於龐大，無法將所有變數列出，若需要詳細資料可至[Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)查看。

 | Country | Description                                       | Designation                        | Variety            |
| ------- | ------------------------------------------------- | ---------------------------------- | ------------------ |
| US      | Pineapple rind, lemon pith and orange blossom ... | Reserve Late Harvest               | Riesling           |
| US      | Much like the regular bottling from 2012, this... | Vintner's Reserve Wild Child Block | Pinot Noir         |
| US      | Soft, supple plum envelopes an oaky structure ... | Mountain Cuvée                     | Cabernet Sauvignon |



## 2.2 Variables

* #### Response variables(imbalance)

 在此資料集中葡萄種類一共有707種，但有些葡萄種類樣本過少，所以選擇預測前六大的葡萄種類。

 |Response variables(Variety)|n(observations)|
|:------:|:-:|
|Pinot Noir|12276|
|Chardonnay|10865|
|Cabernet Sauvignon|8833|
|Red Blend|8237|
|Bordeaux-style Red Blend|6467|
|Riesling|4773|
|**Total**|**51451**|

* #### Predictor variables

 對於喝下葡萄酒之後品酒師的描述。

 | Description                                                  |
| ------------------------------------------------------------ |
| Pineapple rind, lemon pith and orange blossom start off the aromas. The palate is a bit more opulent, with notes of honey-drizzled guava and mango giving way to a slightly astringent, semidry finish. |
| Much like the regular bottling from 2012, this comes across as rather rough and tannic, with rustic, earthy, herbal characteristics. Nonetheless, if you think of it as a pleasantly unfussy country wine, it's a good companion to a hearty winter stew. |
| Slightly reduced, this wine offers a chalky, tannic backbone to an otherwise juicy explosion of rich black cherry, the whole accented throughout by firm oak and cigar box. |

# 3. Model



