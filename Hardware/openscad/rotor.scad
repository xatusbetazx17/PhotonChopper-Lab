// rotor.scad — Parametric scalloped/slotted chopper wheel
// Inspired by a corrugated foil ring. Suitable for STL/DXF export.
// (c) 2025 PhotonChopper-Lab — MIT License

// ===== User parameters =====
outer_d = 120;        // outer diameter (mm)
inner_d = 40;         // inner diameter/hub bore (mm)
thickness = 2.5;      // disk thickness (mm)
N_teeth = 300;        // number of teeth == number of gaps
duty = 0.5;           // gap fraction of pitch [0.3..0.7]
scallop_depth = 2;    // radial scallop amplitude (mm)
hub_d = 20;           // hub clamp bore (mm)
hub_bolt_circle = 28; // for 3x M3 bolts
hub_bolt_d = 3.2;
hub_bolts = 3;

// ===== Derived =====
pitch_deg = 360/N_teeth;
gap_deg = pitch_deg*duty;
tooth_deg = pitch_deg - gap_deg;

module scalloped_radius(angle){
    // Simple cosine scallop around the rim
    // angle in degrees
    amp = scallop_depth;
    base = outer_d/2;
    r = base - amp*(1 - cos( (angle)*2*PI/ pitch_deg))/2;
    circle(r=r);
}

module ring_outline(){
    difference(){
        // outer contour with scallop
        rotate_extrude(convexity=10)
            translate([outer_d/2,0,0]) square([0.01, thickness], center=true); // base
        // inner bore
        circle(d=inner_d);
        // slots
        for(i=[0:N_teeth-1]){
            rotate(i*pitch_deg)
                polygon(points=[
                    [inner_d/2,0],
                    [outer_d/2,0],
                    [outer_d/2,0],
                    [inner_d/2,0]
                ]);
        }
    }
}

// We'll construct slots by subtracting angular windows
module slotted_disc(){
    difference(){
        linear_extrude(height=thickness)
            difference(){
                circle(d=outer_d);
                circle(d=inner_d);
            }
        // subtract gaps
        for(i=[0:N_teeth-1]){
            rotate([0,0,i*pitch_deg + tooth_deg]) // place gap after tooth
                translate([0,0,-1])
                    linear_extrude(height=thickness+2)
                        offset(r=0)
                            arc_sector(inner_d/2, outer_d/2, gap_deg);
        }
    }
}

// helper: 2D arc sector
module arc_sector(r1, r2, ang){
    // ang in degrees, centered at 0 degrees
    rotate(-ang/2)
        difference(){
            circle(r=r2);
            circle(r=r1);
            rotate(ang) translate([-2*r2,-2*r2]) square([4*r2,4*r2]);
            translate([-2*r2,-2*r2]) square([4*r2,4*r2]);
        }
}

module hub_holes(){
    for (i=[0:hub_bolts-1]){
        rotate(i*360/hub_bolts) translate([hub_bolt_circle/2,0,0])
            cylinder(h=thickness+1, d=hub_bolt_d, center=true);
    }
}

// Final assembly
difference(){
    slotted_disc();
    // hub bore
    cylinder(h=thickness+1, d=hub_d, center=true);
    // bolt circle
    hub_holes();
}
