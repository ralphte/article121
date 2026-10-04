// Stylised, procedurally built Blackbird for the design prototypes.
// Proportions follow the published SR-71A three-view: length 32.74 m, span 16.94 m.
// The production site will replace this with a properly modelled glTF.
import * as THREE from 'three';

export const DIM = { length: 32.74, span: 16.94, height: 5.64 };

const L = DIM.length;
const HALF = L / 2;
const NAC_Z = 4.35;      // nacelle centreline, metres from the aircraft centreline
const NAC_R = 1.25;     // nacelle maximum radius
const x = (s) => HALF - s; // station from the nose -> model x (nose points +x)

// Half planform outline as [station, half-width] from nose to tail.
const HALF_OUTLINE = [
  [0, 0], [0.8, 0.2], [2, 0.46], [3.5, 0.74], [5, 1.0], [7, 1.32], [9, 1.64],
  [11, 2.0], [12.5, 2.36], [13.8, 2.76], [14.8, 3.15], [15.2, 3.4],
  [15.6, 5.5], [16.6, 5.95], [18.6, 7.25], [20.2, 8.15], [21.2, 8.44], [22.4, 8.47],
  [26.6, 8.36], [27.8, 8.0], [28.6, 5.5], [28.9, 3.1], [29.5, 1.1],
  [31.2, 0.6], [32.74, 0.22],
];

function planformShape() {
  const right = HALF_OUTLINE.map(([s, w]) => new THREE.Vector2(x(s), -w));
  const left = HALF_OUTLINE.slice(1, -1).reverse().map(([s, w]) => new THREE.Vector2(x(s), w));
  const tailR = new THREE.Vector2(x(L), -0.22), tailL = new THREE.Vector2(x(L), 0.22);
  const pts = [...right, tailR, tailL, ...left];
  // Smooth the hand-placed outline so the chines read as one curve.
  const curve = new THREE.SplineCurve(pts);
  return new THREE.Shape(curve.getSpacedPoints(260));
}

function latheAlongX(profile, segments = 48) {
  // profile: [station, radius] pairs, nose to tail
  const pts = profile.map(([s, r]) => new THREE.Vector2(r, s));
  const g = new THREE.LatheGeometry(pts, segments);
  g.rotateZ(Math.PI / 2);      // lathe y axis -> model -x
  g.translate(HALF, 0, 0);     // station 0 at the nose
  return g;
}

function finGeometry(thick = 0.09) {
  const s = new THREE.Shape();
  s.moveTo(x(25.4), 0);
  s.lineTo(x(30.4), 0);
  s.lineTo(x(30.8), 3.4);
  s.lineTo(x(28.8), 3.4);
  s.closePath();
  const g = new THREE.ExtrudeGeometry(s, { depth: thick, bevelEnabled: false });
  g.translate(0, 0, -thick / 2);
  return g;
}

/**
 * Build the aircraft.
 * opts.skin     material for the airframe
 * opts.glass    material for the canopies
 * opts.dark     material for intakes and nozzles
 * opts.edges    add LineSegments outlines (blueprint look); value is the line material
 * opts.hideFill hide the filled meshes but keep them as occluders
 */
export function buildBlackbird(opts = {}) {
  const skin = opts.skin || new THREE.MeshStandardMaterial({ color: 0x15171b, metalness: 0.5, roughness: 0.55 });
  const glass = opts.glass || new THREE.MeshStandardMaterial({ color: 0x0a0d12, metalness: 0.9, roughness: 0.12 });
  const dark = opts.dark || new THREE.MeshBasicMaterial({ color: 0x020203 });
  const root = new THREE.Group();
  root.name = 'blackbird';
  const parts = {};

  // Wing and chine slab
  const slabDepth = 0.26;
  const slab = new THREE.ExtrudeGeometry(planformShape(), {
    depth: slabDepth, bevelEnabled: true, bevelThickness: 0.1, bevelSize: 0.08, bevelSegments: 2, curveSegments: 1,
  });
  slab.rotateX(-Math.PI / 2);
  slab.translate(0, -slabDepth / 2, 0);
  parts.wing = new THREE.Mesh(slab, skin);

  // Fuselage: a flattened body of revolution sitting through the slab
  const fus = latheAlongX([
    [0, 0], [0.6, 0.12], [2, 0.34], [4, 0.52], [7, 0.7], [10, 0.8], [14, 0.86],
    [22, 0.86], [27, 0.78], [30, 0.58], [32.2, 0.3], [32.74, 0.12],
  ], 40);
  fus.scale(1, 0.78, 1);
  parts.fuselage = new THREE.Mesh(fus, skin);

  // Canopies: pilot and reconnaissance systems officer
  const canopyGeo = new THREE.SphereGeometry(1, 32, 16);
  const c1 = new THREE.Mesh(canopyGeo, glass);
  c1.scale.set(1.6, 0.5, 0.46); c1.position.set(x(8.4), 0.56, 0);
  const c2 = new THREE.Mesh(canopyGeo, glass);
  c2.scale.set(1.25, 0.46, 0.44); c2.position.set(x(10.5), 0.6, 0);
  // Dorsal spine running back from the rear canopy
  const spine = latheAlongX([[10.6, 0], [11.4, 0.34], [16, 0.42], [24, 0.34], [28, 0]], 24);
  spine.scale(1, 1, 0.9); spine.translate(0, 0.48, 0);
  parts.canopy = new THREE.Group();
  parts.canopy.add(c1, c2, new THREE.Mesh(spine, skin));

  // Nacelles with translating inlet spikes
  const nacProfile = [[13.6, 0.98], [13.62, 1.06], [14.6, 1.16], [16.6, NAC_R], [26, NAC_R], [29.4, 1.12], [31.6, 1.0]];
  const spikeProfile = [[11.9, 0], [12.5, 0.17], [13.3, 0.42], [14.3, 0.66], [15.2, 0.68]];
  parts.nacelles = [];
  parts.spikes = [];
  parts.exhausts = [];
  parts.fins = [];
  for (const side of [1, -1]) {
    const g = new THREE.Group();
    g.position.set(0, 0.5, side * NAC_Z);    // sits slightly above the wing plane
    const shell = new THREE.Mesh(latheAlongX(nacProfile, 48), skin);
    const spike = new THREE.Mesh(latheAlongX(spikeProfile, 40), skin);
    const face = new THREE.Mesh(new THREE.CircleGeometry(1.0, 40), dark);
    face.rotation.y = Math.PI / 2; face.position.x = x(14.8); face.userData.isFace = true;
    const nozzle = new THREE.Mesh(new THREE.CircleGeometry(0.98, 40), dark);
    nozzle.rotation.y = -Math.PI / 2; nozzle.position.x = x(31.2); nozzle.userData.isFace = true;
    g.add(shell, spike, face, nozzle);
    // Vertical tail on top of the nacelle, canted 15 degrees inboard
    const fin = new THREE.Mesh(finGeometry(), skin);
    fin.position.set(0, NAC_R * 0.82, 0);
    fin.rotation.x = side * THREE.MathUtils.degToRad(15);
    g.add(fin);
    root.add(g);
    parts.nacelles.push(g);
    parts.spikes.push(spike);
    parts.fins.push(fin);
    parts.exhausts.push(new THREE.Vector3(x(31.6), 0, side * NAC_Z));
  }

  root.add(parts.wing, parts.fuselage, parts.canopy);

  if (opts.edges) {
    const lineMat = opts.edges;
    // Crisp planform outline on the upper and lower wing surfaces
    const loop = planformShape().getSpacedPoints(400);
    for (const y of [slabDepth / 2 + 0.1, -slabDepth / 2 - 0.1]) {
      const pts = loop.map((p) => new THREE.Vector3(p.x, y, -p.y));
      root.add(new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints(pts), lineMat));
    }
    root.traverse((o) => {
      if (o.isMesh && !o.userData.isFace) {
        const e = new THREE.LineSegments(new THREE.EdgesGeometry(o.geometry, opts.edgeAngle || 24), lineMat);
        e.userData.isEdge = true;
        o.add(e);
        if (opts.hideFill) {
          o.material = opts.occluder;
        }
      }
    });
  }

  if (opts.outline) {
    // Inverted hull: back faces pushed out along their normals read as silhouette lines
    const meshes = [];
    root.traverse((o) => { if (o.isMesh && !o.userData.isFace) meshes.push(o); });
    for (const o of meshes) o.add(new THREE.Mesh(o.geometry, opts.outline));
  }

  root.userData.parts = parts;
  return root;
}

/** Flat-colour silhouette material for buildBlackbird({ outline }). Thickness is in metres. */
export function outlineMaterial(color, thickness = 0.07) {
  return new THREE.ShaderMaterial({
    uniforms: { uColor: { value: new THREE.Color(color) }, uThick: { value: thickness } },
    side: THREE.BackSide,
    vertexShader: 'uniform float uThick; void main() { gl_Position = projectionMatrix * modelViewMatrix * vec4(position + normal * uThick, 1.0); }',
    fragmentShader: 'uniform vec3 uColor; void main() { gl_FragColor = vec4(uColor, 1.0); }',
  });
}

/** Afterburner plume: one soft cone per engine with stationary shock diamonds. */
export function buildAfterburners(parts, color = 0xff9a3c) {
  const group = new THREE.Group();
  const uniforms = { uTime: { value: 0 }, uStrength: { value: 1 }, uColor: { value: new THREE.Color(color) } };
  const mat = new THREE.ShaderMaterial({
    uniforms,
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
    vertexShader: /* glsl */`
      varying float vAxial; varying vec3 vN; varying vec3 vV;
      void main() {
        vAxial = 0.5 + position.y / 10.0;            // 0 at the nozzle, 1 at the tip
        vec4 mv = modelViewMatrix * vec4(position, 1.0);
        vN = normalize(normalMatrix * normal); vV = normalize(-mv.xyz);
        gl_Position = projectionMatrix * mv;
      }`,
    fragmentShader: /* glsl */`
      uniform float uTime; uniform float uStrength; uniform vec3 uColor;
      varying float vAxial; varying vec3 vN; varying vec3 vV;
      void main() {
        float facing = pow(abs(dot(normalize(vN), normalize(vV))), 1.6);
        float fade = pow(1.0 - vAxial, 1.7);
        float diamonds = pow(0.5 + 0.5 * cos(vAxial * 40.0), 6.0) * smoothstep(0.75, 0.05, vAxial);
        float flicker = 0.9 + 0.1 * sin(uTime * 37.0 + vAxial * 9.0);
        vec3 core = mix(uColor, vec3(1.0, 0.95, 0.82), diamonds * 0.8 + (1.0 - vAxial) * 0.25);
        float a = (fade * 0.8 + diamonds * 1.1) * facing * flicker * uStrength;
        gl_FragColor = vec4(core * a, a);
      }`,
  });
  const plumes = [];
  for (const p of parts.exhausts) {
    const cone = new THREE.Mesh(new THREE.CylinderGeometry(0.92, 0.3, 10, 40, 24, true), mat);
    cone.rotation.z = Math.PI / 2;           // cylinder +y -> model -x (aft)
    cone.position.copy(p); cone.position.x -= 5;
    group.add(cone); plumes.push(cone);
  }
  group.userData.flicker = (t, strength = 1) => {
    uniforms.uTime.value = t; uniforms.uStrength.value = strength;
    for (const c of plumes) c.visible = strength > 0.01;
  };
  return group;
}
