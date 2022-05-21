function vector hedge_src_pos(const int geometry; const int hedge)
{
    /* Returns the position of the source point of the input hedge. */
    return point(geometry, "P", hedge_srcpoint(geometry, hedge));
}

function vector hedge_dst_pos(const int geometry; const int hedge)
{
    /* Returns the position of the destination point of the input hedge. */
    return point(geometry, "P", hedge_dstpoint(geometry, hedge));
}

function vector hedge_pos_lerp(const int geometry; const int hedge; const float value)
{
    /* Returns a lerped position along the hedge src -> dst */
    return lerp(hedge_src_pos(geometry, hedge), hedge_dst_pos(geometry, hedge), value);
}

function vector hedge_dir(const int geometry; const int hedge)
{
    /* Returns a normalized vector pointing the wireing direction of this hedge. */
    return normalize(hedge_dst_pos(geometry, hedge) - hedge_src_pos(geometry, hedge));
}

function float hedge_length(const int geometry; const int hedge)
{
    /* Returns the length of this hedge. */
    return distance(hedge_src_pos(geometry, hedge), hedge_dst_pos(geometry, hedge));
}

function vector hedge_prim_nrm(const int geometry; const int hedge)
{
    /* Returns the normal of the input hedge's primitive. */
    int hedge_prim = hedge_prim(geometry, hedge);
    return prim_normal(geometry, hedge_prim, 0.5, 0.5);
}

function vector hedge_out(const int geometry; const int hedge)
{
    /* Returns a normalized vector pointing out of the polygon of the hedge. */
    vector pr_nrm = hedge_prim_nrm(geometry, hedge);
    vector hedge_dir = hedge_dir(geometry, hedge);

    return normalize(cross(pr_nrm, hedge_dir));
}

function int inhedgegroup(const int geometry; const string grpname; const int hedge)
{
    /* Returns True/False if a hedge is in an edge group. */
    int src = hedge_srcpoint(geometry, hedge);
    int dst = hedge_dstpoint(geometry, hedge);
    return inedgegroup(geometry, grpname, src, dst);
}

function void sethedgegroup(const int geometry; string grpname; int hedge; int value)
{
    /* Adds/removes an Edge from an Edge group using a hedge. */
    int src = hedge_srcpoint(geometry, hedge);
    int dst = hedge_dstpoint(geometry, hedge);
    setedgegroup(geometry, grpname, src, dst, value);
}

function void set_hedge_position(const int geometry; int hedge; vector pos; string method)
{
    /* Sets the positions of the hedge src and dst points using the input method. */
    setpointattrib(geometry, "P", hedge_srcpoint(geometry, hedge), pos, method);
    setpointattrib(geometry, "P", hedge_dstpoint(geometry, hedge), pos, method);
}