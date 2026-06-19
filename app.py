import React, { useState } from 'react';

const materials = ["玫瑰", "繡球花", "康乃馨", "牡丹", "太陽玫瑰", "向日葵", "大理花", "鬱金香", "小蒼蘭", "雞冠花", "洋桔梗", "風信子", "乒乓菊", "蝴蝶蘭", "星辰花", "陸蓮", "海芋", "紅掌", "大波斯菊", "香水百合", "非洲菊", "龍膽花", "鈴蘭", "鐵線蓮", "罌粟花", "滿天星", "兔尾草", "卡斯比亞", "尤加利葉", "無"];

const paperTypes = ["霧面紙", "反光紙", "金屬紙", "薄紗", "牛皮紙"];

export default function FlowerGenerator() {
  const [config, setConfig] = useState({
    type: '盆花',
    mainA: '玫瑰', colorA: '紅色',
    mainB: '無', colorB: '紅色',
    mainC: '無', colorC: '紅色',
    auxA: '無', colorAuxA: '白色',
    auxB: '無', colorAuxB: '白色',
    leafA: '尤加利葉', colorLeafA: '綠色',
    leafB: '無', colorLeafB: '綠色',
    paper: '霧面紙', paperColor: '米色'
  });

  const generatePrompt = () => {
    const p = config;
    const parts = [
      `一個精緻的永生花${p.type}`,
      `主花採用${p.colorA}${p.mainA}`,
      p.mainB !== '無' ? `搭配${p.colorB}${p.mainB}` : '',
      p.mainC !== '無' ? `以及${p.colorC}${p.mainC}` : '',
      p.auxA !== '無' ? `點綴${p.colorAuxA}${p.auxA}` : '',
      p.leafA !== '無' ? `襯托${p.colorLeafA}${p.leafA}` : '',
      `包裝採用${p.paperColor}${p.paper}`,
      "商業花藝攝影，柔和自然光，景深效果，高細節，8k畫質，精緻質感"
    ].filter(item => item !== '').join("，");
    
    return parts;
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <h1>永生花設計提示詞產生器</h1>
      {/* 簡化範例：僅展示部分選單 */}
      <label>花藝類型：</label>
      <select onChange={(e) => setConfig({...config, type: e.target.value})}>
        <option>盆花</option><option>捧花</option>
      </select>
      
      {/* 你可以依此邏輯擴充其他主花、輔助花、葉材的下拉選單 */}
      
      <div style={{ marginTop: '20px', padding: '15px', background: '#f0f0f0' }}>
        <h3>生成提示詞：</h3>
        <p>{generatePrompt()}</p>
        <button onClick={() => navigator.clipboard.writeText(generatePrompt())}>
          複製提示詞
        </button>
      </div>
    </div>
  );
}
