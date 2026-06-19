import React, { useState } from 'react';

const APP_DATA = {
  flowers: ["厄瓜多玫瑰", "奧斯汀玫瑰", "太陽玫瑰", "康乃馨", "牡丹", "繡球花", "無"], // 省略部分以保持簡潔
  materials: ["滿天星", "卡斯比亞", "兔尾草", "尤加利葉", "雪松", "無"],
  wraps: ["霧面紙", "反光紙", "金屬紙", "薄紗", "牛皮紙"]
};

export default function FlowerGenerator() {
  const [config, setConfig] = useState({
    type: '盆花',
    mainA: '', mainB: '', mainC: '',
    auxA: '', auxB: '',
    leafA: '', leafB: '',
    wrap: ''
  });

  const [prompt, setPrompt] = useState('');

  const generatePrompt = () => {
    const p = `Professional preserved flower ${config.type}, featuring ${config.mainA}, ${config.mainB}, ${config.mainC}, accented with ${config.auxA}, ${config.auxB} and ${config.leafA}, ${config.leafB}, wrapped in ${config.wrap}, high-end floral design, studio lighting, 8k resolution, photorealistic, soft texture, elegant aesthetic.`;
    setPrompt(p);
  };

  return (
    <div className="p-6 max-w-2xl mx-auto bg-gray-50">
      <h1 className="text-2xl font-bold mb-4">永生花設計提示詞生成器</h1>
      
      {/* 類型選擇 */}
      <select onChange={(e) => setConfig({...config, type: e.target.value})} className="w-full p-2 mb-4 border rounded">
        <option value="盆花">盆花</option>
        <option value="捧花">捧花</option>
      </select>

      {/* 花材選擇區 (以主花A為例) */}
      <div className="grid grid-cols-2 gap-4">
        <select onChange={(e) => setConfig({...config, mainA: e.target.value})} className="p-2 border rounded">
          <option>選擇主花A</option>
          {APP_DATA.flowers.map(f => <option key={f} value={f}>{f}</option>)}
        </select>
        <input type="color" className="w-full h-10" onChange={(e) => console.log(e.target.value)} />
      </div>

      {/* 生成與複製按鈕 */}
      <div className="mt-6 flex gap-4">
        <button onClick={generatePrompt} className="bg-pink-500 text-white px-4 py-2 rounded">生成提示詞</button>
        <button onClick={() => navigator.clipboard.writeText(prompt)} className="bg-gray-800 text-white px-4 py-2 rounded">複製提示詞</button>
      </div>

      {/* 顯示結果 */}
      {prompt && <div className="mt-4 p-4 bg-white border border-pink-200 rounded text-sm italic">{prompt}</div>}
    </div>
  );
}
