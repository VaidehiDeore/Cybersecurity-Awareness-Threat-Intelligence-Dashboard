const api=async(path,options={})=>{const r=await fetch(`/api${path}`,{headers:{'Content-Type':'application/json','X-Analyst-Key':'demo-analyst-key',...(options.headers||{})},...options}); if(!r.ok){let e='Request failed';try{e=(await r.json()).detail||e}catch{};throw new Error(e)}return r.json()};
export const getStats=()=>api('/dashboard/stats');
export const getTrends=()=>api('/dashboard/trends');
export const getThreats=(params='')=>api(`/threats${params?`?${params}`:''}`);
export const getThreat=id=>api(`/threats/${id}`);
export const searchIndicator=q=>api(`/indicators/search?q=${encodeURIComponent(q)}`);
export const getAlerts=()=>api('/alerts');
export const updateAlert=(id,status)=>api(`/alerts/${id}/status`,{method:'PUT',body:JSON.stringify({status})});
export const addNote=(id,note)=>api(`/threats/${id}/notes`,{method:'POST',body:JSON.stringify({note})});
export const getVulnerabilities=()=>api('/vulnerabilities');
export const getModules=()=>api('/awareness/modules');
export const getQuiz=()=>api('/quiz');
export const submitQuiz=answers=>api('/quiz/submit',{method:'POST',body:JSON.stringify({answers})});
export const getExecutive=()=>api('/executive/summary');
export const getAttack=()=>api('/attack');
export async function updateAlertStatus(alertId, status) {
  const response = await fetch(
    `${API_BASE_URL}/api/alerts/${encodeURIComponent(alertId)}/status`,
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        status,
      }),
    }
  );

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(
      `Failed to update alert status: ${response.status} ${errorText}`
    );
  }

  return response.json();
}
