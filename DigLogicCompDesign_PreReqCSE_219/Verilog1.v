module george(o, x, Y);
output 0;
input x, Y;
wire or_wire, not_wire;

or ol(or_wire, x, y);
not n1(not_wire, y);
and al(o, or_wire, not_wire);

endmodule // george

